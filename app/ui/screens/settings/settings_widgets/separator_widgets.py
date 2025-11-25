from PyQt6.QtWidgets import QFrame

from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager


class CustomSeparator(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFrameShape(QFrame.Shape.HLine)
        self.setFixedHeight(2)
        
        # Appliquer le thème initial
        self.apply_theme()
        # S'abonner aux changements de thème
        ThemeManager.get_instance().theme_changed.connect(self.apply_theme)
        
    
    def apply_theme(self):
        self.setStyleSheet(f"""
            background-color: {StyleManager.get('LINE_SETTING_COLOR')};
        """)  
   