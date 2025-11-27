# app/core/user_logic.py

"""
Module user_logic.py

Logique métier pour l'onglet utilisateur.
Gère les paramètres utilisateur, notifications et avatar.

Auteur : SethiarWorks
Date : 01-01-2026
"""

import os
from typing import Optional, Dict, Any, Union

from PyQt6.QtGui import QPixmap, QPainter, QPainterPath
from PyQt6.QtCore import Qt


from app.core.settings.settings_manager import SettingsManager


class UserLogic():
    """
    Classe UserLogic

    Encapsule la logique métier pour l'utilisateur :
        - Chargement et sauvegarde des settings
        - Gestion de l'avatar (QPixmap rond)
    """
    
    # DEFAULT_AVATAR_PATH = "app/assets/default_avatar.png"
    
    def __init__(self):
        self.manager: SettingsManager = SettingsManager()
    
    # =======================
    # Chargement / sauvegarde settings
    # =======================
    
    def load_user_settings(self):
        """
        Retourne un dictionnaire avec les valeurs actuelles ou valeurs par défaut.

        Returns:
            dict: {name, email, notifications_enabled, avatar_path}
        """
        return {
            "name": self.manager.get("user_name") or "",
            "email": self.manager.get("user_email") or "",
            "notifications_enabled": self.manager.get("notifications_enabled") 
                                    if self.manager.get("notifications_enabled") is not None else True,
            "avatar_path": self.manager.get("user_avatar") or None
        }
        
        
    def save_user_settings(self, name: str, email:str,
                           notifications_enabled: bool,
                           avatar_path: Optional[str] = None):
        """
        Sauvegarde les paramètres utilisateur.

        Args:
            name (str): Nom de l'utilisateur
            email (str): Email
            notifications_enabled (bool): Notifications activées
            avatar_path (str, optional): Chemin vers l'avatar
        """
        self.manager.set("user_name", name)
        self.manager.set("user_email", email)
        self.manager.set("notifications_enabled", notifications_enabled)
        
        if avatar_path:
            self.manager.set("user_avatar", avatar_path)
        
        self.manager.save()
        
        
    # =======================
    # Avatar
    # =======================
    def get_avatar_pixmap(self, path: Optional[str] = None, size: int = 100) -> QPixmap:
        """
        Retourne un QPixmap à afficher pour l'avatar, redimensionné et rond.

        Args:
            path (str, optional): Chemin vers l'avatar
            size (int, optional): Taille souhaitée en pixels

        Returns:
            QPixmap: Pixmap rond prêt à l'affichage
        """
        
        pixmap_path = path or self.load_user_settings().get("avatar_path") or self.DEFAULT_AVATAR_PATH

        if not os.path.exists(pixmap_path):
            pixmap_path = self.DEFAULT_AVATAR_PATH

        pixmap = QPixmap(pixmap_path)
        return self.get_rounded_pixmap(pixmap, size)
            
        
    def get_rounded_pixmap(self, pixmap: Union[QPixmap, None], size: int = 100) -> QPixmap:
        """
        Transforme un QPixmap en avatar rond.

        Args:
            pixmap (QPixmap | None): Pixmap source
            size (int): Taille en pixels

        Returns:
            QPixmap: Pixmap ronde
        """
        size = int(size) if isinstance(size, (int, float, str)) and str(size).isdigit() else 100

        if not isinstance(pixmap, QPixmap) or pixmap.isNull():
            pixmap = QPixmap(self.DEFAULT_AVATAR_PATH)

        # Redimensionnement
        pixmap = pixmap.scaled(
            size,
            size,
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )

        # Création de la pixmap ronde
        rounded = QPixmap(size, size)
        rounded.fill(Qt.GlobalColor.transparent)

        painter = QPainter(rounded)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        path = QPainterPath()
        path.addEllipse(0, 0, size, size)
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()

        return rounded