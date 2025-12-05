# app/ui/screens/screen_task/theme_column/theme_column_ui.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PyQt6.QtCore import Qt

from app.ui.widgets.system.label import ThemeTitleLabel

from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager

class ThemeColumnUI(QWidget):
    """
    Layout vertical avec bordure + titre.
    
    """
    
    def __init__(self, theme_name: str, parent = None):
        super().__init__(parent)
        
        self.theme_name = theme_name
        
        
        self.build_ui()
        self.apply_theme()
        
        ThemeManager.get_instance().theme_changed.connect(self.apply_theme)
        
        
    def build_ui(self):
        self.setObjectName("ThemeColumn")
        self.setMinimumWidth(200)
        self.setMinimumHeight(200)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        
        self.theme_column_layout = QVBoxLayout()
        self.theme_column_layout.setContentsMargins(20, 20, 20, 20)
        self.theme_column_layout.setSpacing(10)
        
        # Titre
        self.theme_title = ThemeTitleLabel(self.theme_name)
        self.theme_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.theme_column_layout.addWidget(self.theme_title)
        
        # Layout des cartes
        self.tasks_layout = QVBoxLayout()
        self.tasks_layout.setSpacing(20)
        self.theme_column_layout.addLayout(self.tasks_layout)   
        
        self.setLayout(self.theme_column_layout)
        
    
    
    def apply_theme(self):
        self.setStyleSheet(f"""
            #ThemeColumn {{
                font-size: {StyleManager.get_scaled_font("FONT_SIZE_SETTING")};
                background-color: {StyleManager.get('THEME_BG_COLOR')};
                border-radius: {StyleManager.get('BORDER_RADIUS')};
                border: 1px solid #000000;
            }}                   
        """) 
        
        