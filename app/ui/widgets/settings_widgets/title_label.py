from PyQt6.QtWidgets import QLabel

from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager

class TitleLabel(QLabel):
    """
    Label pour les titres de section dans les settings.
    Se met à jour automatiquement lors du changement de thème.
    """
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.apply_theme()
        # Se connecter au signal du ThemeManager
        ThemeManager.get_instance().theme_changed.connect(self.apply_theme)

    
    def apply_theme(self):
        self.setStyleSheet(f"""
            QLabel {{
                font-size: {StyleManager.get_scaled_font('FONT_SIZE_TITLE_SETTING')};
                font-weight: {StyleManager.get('FONT_WEIGHT_BOLD')};
                color: {StyleManager.get('SETTING_TITLE_COLOR')};
            }}
        """)