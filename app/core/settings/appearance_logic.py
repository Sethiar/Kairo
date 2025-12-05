#app/core/appearance_logic.py

"""
Module appearance_logic.py

Contient la logique métier pour l'onglet "Apparence" de l'application.
Gère le thème et la taille de police de manière centralisée.

Auteur : SethiarWorks
Date : 01-01-2026
"""

from enum import Enum
from app.core.settings.settings_manager import SettingsManager
from app.core.settings.theme_manager import ThemeManager


# Enumération des thèmes créés
class Theme(Enum):
    LIGHT = "Light"
    DARK = "Dark"


# Enumération des tailles de polices possibles
class FontSize(Enum):
    SMALL = "Petite"
    NORMAL = "Moyenne"
    LARGE = "Grande"
    

# Classe rendant la logique de la page appearance des settings
class AppearanceLogic:
    """
    Classe AppearanceLogic

    Encapsule la logique métier pour l'onglet apparence.
    Permet de charger et sauvegarder les paramètres d'apparence
    (thème et taille de police) et d'appliquer le thème courant.
    """
    def __init__(self):
        """
        Initialise la logique d'apparence.

        - Crée une instance de SettingsManager pour gérer les paramètres.
        - Récupère l'instance singleton du ThemeManager.
        - Applique le thème actuel au démarrage.
        """
        # Instanciation de SettingsManager
        self.settings = SettingsManager()
        # Instanciation de ThemeManager(Singleton)
        self.theme_manager = ThemeManager.get_instance()
        
        # Chargement du thème au démarrage
        self.apply_current_theme()
    
    
    # Méthode permettant d'appliquer le thème sélectionné
    def apply_current_theme(self):
        """
        Applique le thème actuel défini dans les paramètres.

        Si le paramètre 'theme' n'existe pas, applique 'Light' par défaut.
        """
        # Définition de la variable pour nommer le thème choisi
        theme_str = self.settings.get("theme") or Theme.LIGHT.value
        # Mise en commun avec la valeur de la classe Enum
        theme_enum = Theme.DARK if theme_str.lower() == "dark" else Theme.LIGHT
        # Chargement de la valeur du theme
        self.theme_manager.load_theme(theme_enum.value.lower())
        
    
    # Méthode permettant de charger le thème sauvegarder au démarrage
    def load_settings(self) -> dict:
        """
        Retourne les paramètres d'apparence actuels.

        Returns:
            dict: Contient 'theme' (str) et 'font_size' (str)
        """
        return {
            # Retourne les valeurs choisies pour le thème et la police.
            "theme": self.settings.get("theme") or Theme.LIGHT.value,
            "font_size": self.settings.get("font_size") or FontSize.NORMAL.value
        }
    
    
    # Méthode permettant de sauvegarder le thème de l'application sélectionné.
    def save_settings(self, theme=None, font_size=None):
        """
        Sauvegarde les paramètres d'apparence.

        Applique immédiatement le thème si fourni et met à jour la taille de police.
        Ensuite, persiste les paramètres via SettingsManager.save().

        Args:
            theme (str, optional): Thème à appliquer ('Light' ou 'Dark')
            font_size (str, optional): Taille de police ('Small', 'Normal', 'Large', etc.)
        """
         # Validation thème
         # Vérification de l'existence des themes
        if theme:
            if theme.capitalize() not in Theme._member_names_ and theme.capitalize() not in [t.value for t in Theme]:
                raise ValueError(f"Theme invalide : {theme}")
            self.settings.set("theme", theme)
            # Application immédiate
            self.theme_manager.load_theme("dark" if theme.lower() == "dark" else "light")

        # Validation taille de police
        # Vérification de l'existence des polices
        if font_size:
            if font_size.capitalize() not in FontSize._member_names_ and font_size.capitalize() not in [f.value for f in FontSize]:
                raise ValueError(f"FontSize invalide : {font_size}")
            # Application immédiate
            self.settings.set("font_size", font_size)

        # Sauvegarde finale
        self.settings.save()
        
        