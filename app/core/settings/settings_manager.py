# app/core/settings/settings_manager.py

"""
Module settings_manager.py

Singleton pour gérer les paramètres utilisateurs de l'application.
Permet de lire, modifier et sauvegarder les settings dans un fichier JSON.

Auteur : SethiarWorks
Date : 01-01-2026
"""

import json
import os
from typing import Any


class SettingsManager:
    """
    Gestionnaire des paramètres utilisateur.

    Utilise le pattern Singleton pour garantir une seule instance.
    Permet de stocker des valeurs par défaut et de persister dans un fichier JSON.
    """
    
    _instance = None
    SETTINGS_FILES = "settings.json"
    
    def __new__(cls) -> "SettingsManager":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init()
        return cls._instance
    
        
    def _init(self):
        """
        Initialise les valeurs par défaut et charge les settings depuis le fichier JSON.
        """
        
        self.settings: dict[str, Any] = {
            "user_name": "",
            "user_email": "",
            "notifications_enabled": True,
            "theme": "Clair",
            "font_size": "Moyenne",
            "music_volume": 50,
            "music_files": []
        }
        self.load()
        
        
    # =======================    
    # Accès aux paramètres
    # ======================= 
    
    def get(self, key):
        """
        Retourne la valeur d'un paramètre.

        Args:
            key (str): Nom du paramètre.
            default (Any, optional): Valeur par défaut si le paramètre n'existe pas.

        Returns:
            Any: Valeur du paramètre
        """
        return self.settings.get(key)
    
    def set(self, key, value):
        """
        Définit ou met à jour un paramètre.

        Args:
            key (str): Nom du paramètre.
            value (Any): Valeur à attribuer.
        """
        self.settings[key] = value
    
    
    # =======================  
    # Sauvegarde / chargement    
    # ======================= 
        
    def save(self):
        """
        Sauvegarde les paramètres dans le fichier JSON.

        Gère les exceptions pour éviter les plantages en cas de problème disque.
        """
        try:
            with open(self.SETTINGS_FILES, "w", encoding="utf-8") as f:
                json.dump(self.settings, f , indent=4)
        except Exception as e:
            print(f"[SettingsManager] Impossible de sauvegarder le fichier : {e}")             


    def load(self):
        """
        Charge les paramètres depuis le fichier JSON, si disponible.

        En cas d'erreur, conserve les valeurs par défaut.
        """
        if os.path.exists(self.SETTINGS_FILES):
            try:
                with open(self.SETTINGS_FILES, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    if isinstance(data, dict):
                        self.settings.update(data)
            except Exception as e:
                print(f"[SettingsManager] Impossible de charger le fichier : {e}")
                
                