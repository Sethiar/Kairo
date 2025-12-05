# app/ui/system/text_edit.py


from PyQt6.QtWidgets import QTextEdit

from app.core.settings.theme_manager import ThemeManager
from app.styles.style_manager import StyleManager



class CustomTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Application du style
        self.apply_theme()
        
        # Mise à jour du thème choisi
        ThemeManager.get_instance().theme_changed.connect(self.apply_theme)
        
    
    def apply_theme(self):
        self.setStyleSheet(f"""
           QTextEdit {{
               font-size: {StyleManager.get_scaled_font('FONT_SIZE_SETTING')};
               padding: 6px 15px;
               background-color: {StyleManager.get('INPUT_BACKGROUND_COLOR')};
               color: {StyleManager.get('TEXT_COLOR_1')};
               border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};
               border: 1px solid {StyleManager.get('BORDER_COLOR')};
           }}
        """) 
        
        
 