

import json
import os

class SettingsManager:
    _instance = None
    SETTINGS_FILES = "settings.json"
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init()
        return cls._instance
    
        
    def _init(self):
        
        # Valeurs par défaut
        self.settings = {
            "user_name": "",
            "user_email": "",
            "notifications_enabled": True,  # valeur par défaut
            "theme": "Clair",
            "music_volume": 50,
            "music_files": []
        }
        self.load()
        
    def get(self, key):
        return self.settings.get(key)
    
    def set(self, key, value):
        self.settings[key] = value
        
        
        
    def save(self):
        try:
            with open(self.SETTINGS_FILES, "w", encoding="utf-8") as f:
                json.dump(self.settings, f , indent=4)
        except Exception as e:
            print(f"[SettingsManager] Impossible de sauvegarder le fichier : {e}")             

    def load(self):
        if os.path.exists(self.SETTINGS_FILES):
            try:
                with open(self.SETTINGS_FILES, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.settings.update(data)
            except Exception as e:
                print(f"[SettingsManager] impossible de charger le fichier : {e}")
    