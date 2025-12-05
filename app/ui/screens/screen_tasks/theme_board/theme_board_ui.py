# app/ui/screens/screen_tasks/theme_board/theme_board_ui.py

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QBoxLayout

from PyQt6.QtCore import Qt

from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager



class ThemeBoardUI(QWidget):
    """
    Layout horizontal contenant les ThemeColumn.
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("ThemeBoardUI")
        
        self._build_ui() 
        
        self.apply_theme()
        
        ThemeManager.get_instance().theme_changed.connect(self.apply_theme)
    
        
    def _build_ui(self):
        self.theme_layout = QHBoxLayout()
        self.theme_layout.setDirection(QBoxLayout.Direction.LeftToRight)
        self.theme_layout.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)
        self.theme_layout.setSpacing(20)
        self.theme_layout.setContentsMargins(20, 20, 20, 20)
        
        self.setLayout(self.theme_layout)
        
                
    def apply_theme(self):
        self.setStyleSheet(f"""
            QWidget#ThemeBoardUI {{
                font-size: {StyleManager.get_scaled_font("FONT_SIZE_SETTING")};
                background-color: {StyleManager.get('THEME_BG_COLOR')};
                border-radius: {StyleManager.get('BORDER_RADIUS')};
                border: 1px solid #000000;
            }}                   
        """) 
        
        