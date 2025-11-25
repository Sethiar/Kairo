

from app.core.settings.settings_manager import SettingsManager
from app.core.settings.theme_manager import ThemeManager

class AppearenceLogic:
    """Logique métier pour l'onglet apparence"""
    def __init__(self):
        self.settings = SettingsManager()
        self.theme_manager = ThemeManager.get_instance()
        
        # Chargement du thème au démarrage
        self.apply_current_theme()
    
    
    def apply_current_theme(self):
        theme = self.settings.get("theme") or "Light"
        self.theme_manager.load_theme("dark" if theme.lower() == "dark" else "light")
        
        
    def load_settings(self):
        """Retourne un dict avec les valeurs actuelles ou par défaut"""
        return {
            "theme": self.settings.get("theme") or "Light",
            "font_size": self.settings.get("font_size") or "Normal"
        }

    def save_settings(self, theme=None, font_size=None):
        if theme:
            self.settings.set("theme", theme)
            # Application immédiate du thème
            self.theme_manager.load_theme("dark" if theme.lower() == "dark" else "light")
        if font_size:
            self.settings.set("font_size", font_size)
        self.settings.save()
        
        