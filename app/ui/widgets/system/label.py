# app/ui/widgets/system/label.py

from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import Qt

from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager



class CustomLabel(QLabel):
    """
    Label thématisé : applique le thème et se met à jour sur changement de thème.
    """
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        self.setObjectName("CustomLabel")   
        # Suppression border natif
        self.setFrameShape(QLabel.Shape.NoFrame)
        
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, False)
        # Application du thème
        self.apply_theme()
        # Connecter le signal du ThemeManager
        ThemeManager.get_instance().theme_changed.connect(self.apply_theme)

        
    def apply_theme(self):
        self.setStyleSheet(f"""
            QLabel#CustomLabel {{
                font-size: {StyleManager.get_scaled_font('FONT_SIZE_SETTING')};
                color: {StyleManager.get('TEXT_COLOR_1')};
                padding: 2px 0;
            }}
        """)    


class TitleLabel(CustomLabel):
    """
    Label pour les titres de section dans les settings.
    """
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        # safe d'appeler ici, sous-classe déjà initialisée
        self.apply_theme()

    def apply_theme(self):
        self.setStyleSheet(f"""
            QLabel#TitleLabel {{
                font-size: {StyleManager.get_scaled_font('FONT_SIZE_TITLE_SETTING')};
                font-weight: {StyleManager.get('FONT_WEIGHT_BOLD')};
                color: {StyleManager.get('SETTING_TITLE_COLOR')};
            }}
        """)


class SubtitleLabel(CustomLabel):
    """
    Label pour sous-titres ou textes secondaires.
    """
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        
        self.setObjectName("SubtitleLabel")
        self.apply_theme()

    def apply_theme(self):
        self.setStyleSheet(f"""
            QLabel#SubtitleLabel {{
                background: transparent;
                font-size: {StyleManager.get_scaled_font('FONT_SIZE_SETTING')};
                font-weight: {StyleManager.get('FONT_WEIGHT_SEMIBOLD')};            
                color: {StyleManager.get('TEXT_COLOR_1')};
            }}     
        """)
        

class ThemeTitleLabel(QLabel):
    """
    Label pour les titres de la colonne des thèmes.
    """
    def __init__(self, text="", parent=None):
        super().__init__(text, parent)
        
        self.setObjectName("ThemeTitleLabel")
        self.apply_theme()
        
    def apply_theme(self):
        self.setStyleSheet(f"""
            QLabel#ThemeTitleLabel {{
                background: {StyleManager.get('CARD_BG_COLOR')};
                font-size: {StyleManager.get('FONT_THEME_TITLE')};
                font-weight: {StyleManager.get('FONT_WEIGHT_SEMIBOLD')};
                border-radius: {StyleManager.get('BORDER_RADIUS')};
                padding: 10px;                 
            }}
        """)