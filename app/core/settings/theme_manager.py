# app/core/settings/theme_manager.py

"""
Module theme_manager.py

Singleton pour la gestion des thèmes et de la taille de police de l'application.
Émet un signal `theme_changed` lorsqu'un thème ou une police est modifié.

Auteur : SethiarWorks
Date : 01-01-2026
"""

import json
from pathlib import Path
from typing import Literal, Optional

from PyQt6.QtCore import QObject, pyqtSignal

from app.styles.style_manager import StyleManager

FontScale = Literal["Small", "Normal", "Big"]


class ThemeManager(QObject):
    """
    Gestionnaire de thèmes et de taille de police.

    - Singleton accessible via `get_instance()`
    - Charge les fichiers JSON de thème et applique les styles via StyleManager
    - Émet `theme_changed` pour notifier l'UI
    """
    theme_changed = pyqtSignal()
    
    _instance: Optional["ThemeManager"] = None
    THEME_DIR = Path("app/styles/themes")
    
    @classmethod
    def get_instance(cls) -> "ThemeManager":
        """Retourne l'instance unique (singleton) de ThemeManager."""
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        super().__init__()
        self.current_theme = "Light"
    
    
    # =======================  
    # Thème
    # ======================= 
    def set_theme(self, theme_name: str):
        """
        Applique un thème.

        Args:
            theme_name (str): Nom du thème (ex: 'Light', 'Dark')
        """
        self.current_theme = theme_name.capitalize()
        self.load_theme(self.current_theme)
        
        
    def load_theme(self, theme_name: str):
        """
        Charge un thème depuis un fichier JSON et l'applique via StyleManager.

        Émet le signal `theme_changed` après application.

        Args:
            theme_name (str): Nom du thème
        """
        theme_file = self.THEME_DIR / f"{theme_name.lower()}.json"

        if not theme_file.exists():
            print(f"[ThemeManager] Fichier de thème introuvable : {theme_file}")
            return

        try:
            with open(theme_file, "r", encoding="utf-8") as f:
                data = json.load(f)
            StyleManager.update(data)
            self.theme_changed.emit()
        except Exception as e:
            print(f"[ThemeManager] Impossible de charger le thème : {e}")    
    
    
    # -------------------------
    # Taille de police
    # -------------------------
    def set_font_scale(self, scale: FontScale):
        """
        Applique la taille de police.

        Args:
            scale (FontScale): 'Small', 'Normal' ou 'Big'
        """
        try:
            StyleManager.set_font_scale(scale)
            self.theme_changed.emit()
        except Exception as e:
            print(f"[ThemeManager] set_font_scale error: {e}")

    # -------------------------
    # Chargement des paramètres utilisateur
    # -------------------------
    def load_user_settings(self, settings_file: Path | None = None):
        """
        Charge les paramètres utilisateur (thème et taille de police)
        depuis un fichier JSON et applique les valeurs.

        Args:
            settings_file (Path | None): Chemin du fichier JSON. Par défaut 'settings.json'
        """
        if settings_file is None:
            settings_file = Path("settings.json")

        if not settings_file.exists():
            return

        try:
            with open(settings_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            theme = data.get("theme", "Light")
            font = data.get("font_size", "Normal")

            # Appliquer le thème et la police
            self.set_theme(theme)
            self.set_font_scale(font)

        except Exception as e:
            print(f"[ThemeManager] Erreur chargement paramètres utilisateur : {e}")
            
            