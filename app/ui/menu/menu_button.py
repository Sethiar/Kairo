from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import pyqtSignal, Qt

from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager


class MenuButton(QPushButton):
    
    clicked_with_id = pyqtSignal(str)
    
    def __init__(self, text, screen_id, parent=None):
        super().__init__(text, parent)
        self.screen_id = screen_id
        self.active = False
        
        # Applique le style de base
        self._apply_base_style()
        self.clicked.connect(self._emit_id)
        
        # Connexion au changement de scale
        ThemeManager.get_instance().theme_changed.connect(self._update_font_scale)
        
        
    def _emit_id(self):
        self.clicked_with_id.emit(self.screen_id)
        
    
    def _update_font_scale(self):
        """Rafraîchit seulement la taille de police selon le scale actuel"""
        font_size = StyleManager.get_scaled_font("FONT_SIZE_BULLET")
        self.setStyleSheet(self._base_style_template.format(font_size=font_size, active=self.active))
               
    
    def _apply_base_style(self):
        font_size = StyleManager.get_scaled_font("FONT_SIZE_BULLET")
        self.active = False
        self._base_style_template = """
            QPushButton {{
                padding: 12px 20px;
                border-radius: 10px;
                font-size: {font_size};
                font-weight: 600;
                color: white;
                background: transparent;
            }}
            QPushButton:hover {{
                background: #33475B;
            }}
        """
        self.setStyleSheet(self._base_style_template.format(font_size=font_size, active=False))         


    def set_active(self, is_active: bool):
        self.active = is_active
        font_size = StyleManager.get_scaled_font("FONT_SIZE_BULLET")
        if is_active:
            style = """
                QPushButton {{
                    padding: 12px 20px;
                    border-radius: 10px;
                    font-size: {font_size};
                    font-weight: 700;
                    color: #FFF;
                    background: #1B2838;
                }}
            """.format(font_size=font_size)
            self.setStyleSheet(style)
        else:
            self._apply_base_style()