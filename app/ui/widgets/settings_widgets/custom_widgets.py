from PyQt6.QtWidgets import QComboBox, QListView, QLineEdit

from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager



class CustomLineEdit(QLineEdit):
    def __init__(self, width=250, parent=None):
        super().__init__(parent)
        self.setFixedWidth(width)
        
        # Appliquer le thème au chargement
        self.apply_theme()
        
        # Connexion au changement de thème
        ThemeManager.get_instance().theme_changed.connect(self.apply_theme)
        
    def apply_theme(self):    
        self.setStyleSheet(f"""
            QLineEdit {{ 
                padding: 6px 8px;
                font-size: {StyleManager.get('FONT_SIZE_SETTING')};
                background-color: {StyleManager.get('INPUT_BACKGROUND_COLOR')};
                border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};
                border: 1px solid {StyleManager.get('LINE_SETTING_COLOR')};
            }}
        """)
        
        
class CustomComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # vue personnalisée
        self.view = QListView()
        self.setView(self.view)
        
        # Applique le style
        self.apply_theme()
        # Mise à jour dynamique du changement de thème
        ThemeManager.get_instance().theme_changed.connect(self.apply_theme)
        
        
    def apply_theme(self):

        # Style du menu (QListView)
        self.view.setStyleSheet(f"""
            QListView {{
                background-color: {StyleManager.get('BACKGROUND_COLOR_COMBO')};
                border: 1px solid {StyleManager.get('BORDER_COLOR')};
                border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};
                padding: 4px;
            }}
            
            QListView::item:selected {{
                background-color: {StyleManager.get('BG_DISABLED_COLOR')};
                color:{StyleManager.get('TEXT_COLOR_1')}
            }}
        """)


        # ----------------------
        # Style du QComboBox principal
        # ----------------------
        self.setStyleSheet(f"""
            QComboBox {{
                font-size: {StyleManager.get_scaled_font('FONT_SIZE_SETTING')};
                /* espace pour la flèche externe */
                padding: 6px 30px 6px 10px; 
                color:{StyleManager.get('TEXT_COLOR_1')};
                background-color: {StyleManager.get('INPUT_BACKGROUND_COLOR')};
                border: 1px solid {StyleManager.get('BORDER_COLOR')};
                border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};
            }}

            /* Masque la flèche native */
            QComboBox::drop-down {{
                width: 0px;
                border: none;
            }}

            /* Items du menu */
            QComboBox QAbstractItemView::item {{
                padding: 8px 10px;
                background-color: none;
                font-size: {StyleManager.get_scaled_font('FONT_SIZE_SETTING')};
                border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};
            }}
        """)

        