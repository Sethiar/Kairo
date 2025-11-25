from PyQt6.QtCore import QObject, pyqtSignal

from pathlib import Path
import json

from app.styles.style_manager import StyleManager


class ThemeManager(QObject):
    theme_changed = pyqtSignal()
    
    _instance = None
    THEME_DIR = Path("app/styles/themes")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def __init__(self):
        super().__init__()
        self.current_theme = "Light"
    
    # -------------------------
    # Appelé par l’utilisateur
    # -------------------------
    def set_theme(self, theme_name: str):
        self.current_theme = theme_name.lower()
        self.load_theme(self.current_theme)
    
    #--------------------------
    # Dans ThemeManager
    #--------------------------
    def set_font_scale(self, scale: str):
        try:
            StyleManager.set_font_scale(scale)
            self.theme_changed.emit()
        except Exception as e:
            print(f"[ThemeManager] set_font_scale error: {e}")
    
    
    # -------------------------
    # Chargement du JSON
    # -------------------------
    def load_theme(self, theme_name: str):
        theme_file = self.THEME_DIR / f"{theme_name.lower()}.json"
        
        if not theme_file.exists():
            print(f"[ThemeManager] Fichier de thème introuvable : {theme_file}")
            return
        try:
            with open(theme_file, "r", encoding="utf-8") as f:
                data = json.load(f)
                StyleManager.update(data)
        except Exception as e:
            print(f"[ThemeManager] Impossible de charger le thème : {e}")
        
        self.theme_changed.emit()
        
    
    # -------------------------
    # Gestion de la taille de police
    # -------------------------
    def set_font_scale(self, scale: str):
        """scale = Small | Normal | Big"""
        StyleManager.set_font_scale(scale)
        self.theme_changed.emit()
        
        
    # -------------------------
    # Chargement des paramètres au démarrage
    # -------------------------
    def load_user_settings(self):
        settings_file = Path("settings.json")

        if not settings_file.exists():
            return

        try:
            with open(settings_file, "r", encoding="utf-8") as f:
                data = json.load(f)

            theme = data.get("theme", "Light")
            font = data.get("font_size", "Normal")

            # Charger d'abord le thème
            self.set_theme(theme)

            # Puis la police
            self.set_font_scale(font)

        except Exception as e:
            print(f"[ThemeManager] Erreur chargement paramètres utilisateur : {e}")



