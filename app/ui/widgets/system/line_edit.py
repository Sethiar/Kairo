# app/ui/widgets/system/line_edit.py


"""
Ce fichier donne une base de QLineEdit adaptée pour l'application Kairo.


Auteur : Lefetey Arnaud
01-01-2026
"""


from PyQt6.QtWidgets import QLineEdit



from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager


class CustomLineEdit(QLineEdit):
    def __init__(self, width=250, parent=None):
        super().__init__(parent)
        self.setFixedWidth(width)
        
        # Appliquer le thème au changement
        self.apply_theme()
        
        # Connexion au changement de thème
        ThemeManager.get_instance().theme_changed.connect(self.apply_theme)
        
    
    def apply_theme(self):
        self.setStyleSheet(f"""
            QLineEdit {{
                padding: 6px 10px;
                font-size: {StyleManager.get('FONT_SIZE_SETTING')};
                background-color: {StyleManager.get('INPUT_BACKGROUND_COLOR')};
                border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};
                border: 1px solid {StyleManager.get('LINE_SETTING_COLOR')};
            }}
        """)
    