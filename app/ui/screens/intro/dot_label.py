# app/ui/screens/intro/dot_label.py

"""
DotLabel
--------
Petit indicateur circulaire utilisé pour représenter un état actif/inactif
dans une progression (tutoriel, étapes, pagination, etc.).

Le style (couleurs, taille) est entièrement piloté par StyleManager
et se met automatiquement à jour lorsque le thème change.

Auteur : SethiarWorks
Date : 01-01-2026
"""

from PyQt6.QtWidgets import QLabel

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QColor, QPainter, QBrush

from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager



class DotLabel(QLabel):
    """
    Indicateur circulaire actif/inactif entièrement basé sur le thème.
    """
    def __init__(self, active: bool = False, parent=None):
        super().__init__()
        
        self.active = active
        
        # Récupération initiale du style
        self._load_theme_values()
        
        # Taille fixe du widget
        self.setFixedSize(QSize(self.dot_size, self.dot_size))
        
        # Réagit aux changements de thème
        ThemeManager.get_instance().theme_changed.connect(self._on_theme_changed)
        
        
    # =======================
    # Screen management
    # ======================= 
    def _load_theme_values(self):
        """
        Charge les valeurs issues du thème via StyleManager.
        """
        # Couleurs
        self.active_color = StyleManager.get('PRIMARY_COLOR')
        self.inactive_color = StyleManager.get('SECONDARY_COLOR')
        # Taille
        self.dot_size = StyleManager.get('DOT_SIZE')
    
    
    def _on_theme_changed(self):
        """
        Callback declenché à chaque changement de thème.
        Recharge les valeurs puis redessine le widget.
        """
        self._load_theme_values()
        self.setFixedSize(QSize(self.dot_size, self.dot_size))

        self.update()
    
    
    # =======================
    # External API
    # =======================
    def set_active(self, active: bool):
        """Change l'état actif/inactif du point et déclenche un redraw."""
        self.active = active
        self.update()
    
    
    # =======================
    # Rendering
    # =======================
        
    def paintEvent(self, event):
        """Dessine un cercle plein basé sur l'état actif et le thème."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        color_hex = self.active_color if self.active else self.inactive_color
        painter.setBrush(QBrush(QColor(color_hex)))
        painter.setPen(Qt.PenStyle.NoPen)

        painter.drawEllipse(0, 0, self.dot_size, self.dot_size)
        
        