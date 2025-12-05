# app/core/user_logic.py

"""
Module user_logic.py

Logique métier pour la gestion des paramètres utilisateur :
- Chargement et sauvegarde des paramètres
- Gestion de l'avatar utilisateur (image circulaire)

Auteur : SethiarWorks
Date : 01-01-2026
"""

import os
from typing import Optional, Union

from PyQt6.QtGui import QPixmap, QPainter, QPainterPath
from PyQt6.QtCore import Qt


from app.core.settings.settings_manager import SettingsManager


class UserLogic():
    """
    Classe UserLogic

    Gère :
        - L'interaction avec le SettingsManager
        - Les paramètres utilisateur (nom, email, notifications)
        - La création et la mise en forme de l'avatar (pixmap circulaire)
    """
    
    
    # Chemin par défaut vers l'avatar placeholder
    # DEFAULT_AVATAR_PATH = "app/assets/default_avatar.png"
    
    def __init__(self):
        # Instanciation de SettingsManager
        self.manager: SettingsManager = SettingsManager()
    
    
    # =================================
    # Chargement / sauvegarde settings
    # =================================
    
    # Chargement des valeurs enregistrées
    def load_user_settings(self):
        """
        Retourne un dictionnaire avec les valeurs actuelles ou valeurs par défaut.

        Returns:
            dict: Contient les champs :
                - name (str)
                - email (str)
                - notifications_enabled (bool)
                - avatar_path (str | None)
        """
        
        # Valeurs à retourner sous forme de dictionnaire
        return {
            "name": self.manager.get("user_name") or "",
            "email": self.manager.get("user_email") or "",
            "notifications_enabled": self.manager.get("notifications_enabled") 
                                    if self.manager.get("notifications_enabled") is not None else True,
            "avatar_path": self.manager.get("user_avatar") or None
        }
        
        
    # Sauvegarde des valeurs enregistrées    
    def save_user_settings(self, name: str, email:str,
                           notifications_enabled: bool,
                           avatar_path: Optional[str] = None):
        """
        Sauvegarde les paramètres utilisateur.

        Args:
            name (str): Nom de l'utilisateur.
            email (str): Adresse email.
            notifications_enabled (bool): Activation des notifications.
            avatar_path (str | None): Chemin vers l'image de l'avatar.
        """
        # Récupération de la variable name
        self.manager.set("user_name", name)
        # Récupération de la variable email
        self.manager.set("user_email", email)
        # Récupération de la variable notification True/False
        self.manager.set("notifications_enabled", notifications_enabled)
        
        # Vérification du chemin de la photo de l'avatar
        if avatar_path:
            self.manager.set("user_avatar", avatar_path)
        
        # Méthode pour sauvegarder les données
        self.manager.save()
        
        
    # =======================
    # Avatar
    # =======================
    def get_avatar_pixmap(self, path: Optional[str] = None, size: int = 100) -> QPixmap:
        """
        Retourne un avatar circulaire prêt à l'affichage.

        Args:
            path (str | None): Chemin manuel vers une image. Si None,
                utilise l'avatar enregistré dans les paramètres utilisateur.
            size (int): Taille (carrée) en pixels du rendu final.

        Returns:
            QPixmap: Avatar circulaire redimensionné.
        """
        
        # Chemin de la photo de l'avatar
        pixmap_path = path or self.load_user_settings().get("avatar_path") or self.DEFAULT_AVATAR_PATH
        
        # Vérification de l'existence du fichier
        if not os.path.exists(pixmap_path):
            # Si non fichier par défaut
            pixmap_path = self.DEFAULT_AVATAR_PATH
        
        # Chargement de l'image source
        pixmap = QPixmap(pixmap_path)
        
        # Retour de l'image
        return self.get_rounded_pixmap(pixmap, size)
            
        
    def get_rounded_pixmap(self, pixmap: Union[QPixmap, None], size: int = 100) -> QPixmap:
        """
        Transforme un QPixmap en avatar circulaire.

        Args:
            pixmap (QPixmap | None): Image source. Si invalide, avatar par défaut.
            size (int): Taille finale (carrée) en pixels.

        Returns:
            QPixmap: Image circulaire avec rendu anti-aliasé.
        """
        # Conversion robuste du paramètre size
        try:
            size = int(size)
        except:
            size = 100
            
        # Si la pixmap est invalide, charge l'avatar par défaut
        if not isinstance(pixmap, QPixmap) or pixmap.isNull():
            pixmap = QPixmap(self.DEFAULT_AVATAR_PATH)

        # Redimensionnement en carré, en conservant un remplissage propre
        pixmap = pixmap.scaled(
            size,
            size,
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )
        
        # Pixmap finale transparente qui accueillera l’image ronde
        rounded = QPixmap(size, size)
        rounded.fill(Qt.GlobalColor.transparent)
        

        # --- Découpage rond de l’image ---
        
        # Création du painter chargé de dessiner dans la pixmap finale
        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Chemin circulaire servant de masque
        path = QPainterPath()
        path.addEllipse(0, 0, size, size)
        
        # Application du masque sur toute la pixmap
        painter.setClipPath(path)
        
        # Dessin de l’image redimensionnée à l’intérieur du masque
        painter.drawPixmap(0, 0, pixmap)
        
        # Finalisation (fermeture propre du painter)
        painter.end()

        return rounded