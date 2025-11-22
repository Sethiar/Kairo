
import os

from PyQt6.QtGui import QPixmap, QPainter, QBrush, QPainterPath
from PyQt6.QtCore import Qt


from app.core.settings.settings_manager import SettingsManager


class UserLogic():
    """Logique métier pour l'onglet utilisateur"""
    
    def __init__(self):
        self.manager = SettingsManager()
        
    
    # ------------------------------
    # Chargement / sauvegarde settings
    # ------------------------------
    
    def load_user_settings(self):
        """Retourne un dict avec les valeurs actuelles ou valeurs par défaut"""
        return {
            "name": self.manager.get("user_name") or "",
            "email": self.manager.get("user_email") or "",
            "notifications_enabled": self.manager.get("notifications_enabled") if self.manager.get("notifications_enabled") is not None else True,
            "avatar_path": self.manager.get("user_avatar") or None
        }
        
        
    def save_user_settings(self, name, email, notifications_enabled, avatar_path=None):
        self.manager.set("user_name", name)
        self.manager.set("user_email", email)
        self.manager.set("notifications", notifications_enabled)
        
        if avatar_path:
            self.manager.set("user_avatar", avatar_path)
        
        self.manager.save()
        
        
    # ------------------------------
    # Avatar
    # ------------------------------
    def get_avatar_pixmap(self, path=None, size=100):
        """Retourne un QPixmap à afficher pour l'avatar, redimensionné automatiquement"""
        
        settings = self.load_user_settings()
        avatar_path = settings.get("avatar_path")

        if path and os.path.exists(path):
            pixmap = QPixmap(path)
        else:
            settings = self.load_user_settings()
            avatar_path = settings.get("avatar_path")
            if avatar_path and os.path.exists(avatar_path):
                pixmap = QPixmap(avatar_path)
            else:
                pixmap = QPixmap("app/assets/default_avatar.png")

        return self.get_rounded_pixmap(pixmap, size)
            
        
    def get_rounded_pixmap(self, pixmap, size):
        """Retourne un QPixmap rond."""
        
        size = int(size) if isinstance(size, (int, float, str)) and str(size).isdigit() else 100
    
        if not isinstance(pixmap, QPixmap):
            pixmap = QPixmap("app/assets/default_avatar.png")
  
        pixmap = pixmap.scaled(
            size,
            size,
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )

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

      
        
                