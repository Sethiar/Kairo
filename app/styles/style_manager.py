"""
StyleManager
============

Le module `StyleManager` centralise toutes les variables de style (design tokens)
utilisées dans l'application. Il combine automatiquement les dictionnaires
définis dans les fichiers du dossier `app/styles/vars/`.

Son objectif est de fournir un point d’accès unique aux valeurs de style
(couleurs, polices, espacements, bordures, menus, widgets, etc.) pour garantir :

- une cohérence visuelle totale de l’application,
- une maintenance simplifiée,
- une modification rapide des thèmes (dark mode, branding personnalisé),
- aucune duplication de valeur dans le code ou les styles.


Usage
-----

Récupération d’une variable :
    >>> from app.styles.style_manager import StyleManager
    >>> bg = StyleManager.get("BACKGROUND_COLOR")

Utilisation dans un stylesheet :
    widget.setStyleSheet(f\"\"\"
        background-color: {StyleManager.get('BACKGROUND_COLOR')};
        color: {StyleManager.get('TEXT_COLOR_1')};
        border-radius: {StyleManager.get('BORDER_RADIUS')}px;
    \"\"\")

Ajout d’une nouvelle variable :
- ajouter la valeur dans un des dictionnaires du dossier `vars/`
- aucune modification du StyleManager n’est nécessaire

Ce module agit comme un “global registry” pour tous les design tokens
de l’application.
"""


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
    VARS = {
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

    # Récupère la valeur d'une variable de style par son nom
    @staticmethod
    def get(key):
        """
        Récupère la valeur d'une variable de style par son nom.
        
        Parameters
        ----------
        key : str
            Le nom de la variable de style à récupérer.
            
        Returns
        -------
        Any
            La valeur de la variable de style (str, int, float selon la variable). 
        
        Raises
        ------
        KeyError
            Si la variable demandée n'existe pas.       
        """
        
        return StyleManager.VARS[key]
    
    @staticmethod
    def update(values: dict):
        """Met à jour les valeurs existantes ou ajoute de nouvelles clés"""
        StyleManager.VARS.update(values)
    
