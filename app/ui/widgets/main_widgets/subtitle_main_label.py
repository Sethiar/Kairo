from PyQt6.QtWidgets import QLabel


from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager

class SubtitleMainLabel(QLabel):
    def __init__(self, label_text, parent=None):
        super().__init__(label_text, parent)
        self.apply_theme()
        
        ThemeManager.get_instance().theme_changed.connect(self.apply_theme)
    
    def apply_theme(self):
        self.setStyleSheet(f"""
            QLabel {{
                font-size: {StyleManager.get_scaled_font('FONT_SIZE_SETTING')};
                font-weight: {StyleManager.get('FONT_WEIGHT_SEMIBOLD')};            
                color: {StyleManager.get('TEXT_COLOR_2')};
            }}     
        """)
               