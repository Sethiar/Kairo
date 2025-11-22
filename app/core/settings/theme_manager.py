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
                StyleManager.VARS.update(data)
        except Exception as e:
            print(f"[ThemeManager] Impossible de charger le thème : {e}")
        
        self.theme_changed.emit()    