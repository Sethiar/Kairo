from typing import Any, Dict

from app.styles.vars_borders import VARS_BORDERS
from app.styles.vars_colors import VARS_COLORS
from app.styles.vars_effects import VARS_EFFECTS
from app.styles.vars_fonts import VARS_FONTS
from app.styles.vars_inputs import VARS_INPUTS
from app.styles.vars_layouts import VARS_LAYOUTS
from app.styles.vars_menus import VARS_MENUS
from app.styles.vars_spacing import VARS_SPACING
from app.styles.vars_widgets import VARS_WIDGETS


# Classe qui centralise toutes les variables de style
class StyleManager:
    VARS: Dict[str, Any] = {
        **VARS_BORDERS,
        **VARS_COLORS,
        **VARS_EFFECTS,
        **VARS_FONTS,
        **VARS_INPUTS,
        **VARS_LAYOUTS,
        **VARS_MENUS,
        **VARS_SPACING,
        **VARS_WIDGETS,
    }
    
    
    # Méthode pour gérer les tailles de police.
    # Valeur par défaut : normal
    FONT_SCALE_MAP = {
        "Petite": 0.9,
        "Normal": 1.0,
        "Grande": 1.1,
    }

    current_scale = 1.0
    
    # Conserver les valeurs sources (non transformées) afin de pouvoir re-calculer proprement.
    _SOURCE_FONTS: Dict[str, Any] = {}
    
    @staticmethod
    def _ensure_source_fonts_cached():
        # cache les valeurs initiales une fois
        if StyleManager._SOURCE_FONTS:
            return
        for k, v in StyleManager.VARS.items():
            if k.startswith("FONT_"):
                StyleManager._SOURCE_FONTS[k] = v
                
    
    @staticmethod
    def set_font_scale(scale_name: str):
        """scale_name: 'Petite' | 'Normal' | 'Grande'"""
        if scale_name not in StyleManager.FONT_SCALE_MAP:
            raise ValueError(f"Scale '{scale_name}' invalide.")
        
        StyleManager._current_scale = StyleManager.FONT_SCALE_MAP[scale_name]
        StyleManager._apply_scaled_fonts()
        
    
    @staticmethod
    def _apply_scaled_fonts():
        """Recalcul des tailes de police en fonction de la taille choisie."""    
        
        """Recalcule toutes les clés FONT_* à partir des sources et du _current_scale."""
        StyleManager._ensure_source_fonts_cached()
        scale = StyleManager._current_scale
        updated = {}
        for key, raw in StyleManager._SOURCE_FONTS.items():
            # raw peut être "16px" ou un int
            if isinstance(raw, str) and raw.endswith("px"):
                base = int(raw.replace("px", ""))
                updated[key] = f"{int(round(base * scale))}px"
            elif isinstance(raw, (int, float)):
                updated[key] = f"{int(round(raw * scale))}px"
            else:
                # fallback : on laisse tel quel
                updated[key] = raw
        StyleManager.VARS.update(updated)
        # debug
        print(f"[StyleManager] polices recalculées (scale={scale})")     
    
    
    @staticmethod
    def get_scaled_font(key: str) -> str:
        """Renvoie une string 'Npx' en tenant compte du scale."""
        # si la clé existe et est déjà en px -> retour direct
        val = StyleManager.VARS.get(key)
        if isinstance(val, str) and val.endswith("px"):
            return val
        # si non présent dans VARS mais présent dans source -> recalculer
        StyleManager._ensure_source_fonts_cached()
        src = StyleManager._SOURCE_FONTS.get(key)
        if isinstance(src, str) and src.endswith("px"):
            base = int(src.replace("px", ""))
            scaled = int(round(base * StyleManager._current_scale))
            return f"{scaled}px"
        if isinstance(src, (int, float)):
            scaled = int(round(src * StyleManager._current_scale))
            return f"{scaled}px"
        # dernier recours
        raise KeyError(f"StyleManager: clé de police inconnue '{key}'")

    @staticmethod
    def get(key: str, default=None):
        return StyleManager.VARS.get(key, default)

    @staticmethod
    def update(values: Dict[str, Any]):
        StyleManager.VARS.update(values)
        # si on a mis à jour des FONT_* dans le thème json, mettre à jour le cache source
        # (on préfère conserver les valeurs fournies dans le JSON comme "source")
        for k in list(values.keys()):
            if k.startswith("FONT_"):
                StyleManager._SOURCE_FONTS[k] = values[k]