# app/ui/widgets/system/combo.py

from PyQt6.QtWidgets import QComboBox, QListView

from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager


class CustomComboBox(QComboBox):
    """
    QComboBox personnalisé qui applique automatiquement le style
    au widget et à sa popup, et se met à jour lors du changement de thème.
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Vue personnalisée
        self.setView(QListView())
        
        # Application du style
        self.apply_theme()
        
        # Mise à jour du thème choisi
        ThemeManager.get_instance().theme_changed.connect(self.apply_theme)
        
    def apply_theme(self):
        """
        Méthode qui applique le style au QComboBox et à sa popup.
        """
        self.setStyleSheet(f"""
            QComboBox {{
                background-color: {StyleManager.get('INPUT_BACKGROUND_COLOR')};
                font-size: {StyleManager.get_scaled_font('FONT_SIZE_SETTING')};
                /* espace pour la flèche externe */
                padding: 6px 20px 6px 15px;
                color: {StyleManager.get('TEXT_COLOR_1')};
                border: 1px solid {StyleManager.get('BORDER_COLOR')};
                border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};                
            }}
            
            /* Masque la flèche native */
            QComboBox::drop-down {{
                width: 0px;
                border: none;
            }}
        """)
        
        # Style de la popup
        self._apply_popup_style()
        
        
    def _apply_popup_style(self):    
        """
        Méthode qui applique le style à la QAbstractItemView (popup).
        """
        view = self.view()
        view.setStyleSheet(f"""
                           
            /* Affichage des items*/                                  
            QListView {{
                background-color: {StyleManager.get('INPUT_BACKGROUND_COLOR')};
                border: 1px solid {StyleManager.get('BORDER_COLOR')};
                selection-background-color: {StyleManager.get('HOVER_COLOR')};
                border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};
                outline: 0;
            }}
            
            /* Items du menu */
            QListView::item {{
                background-color: transparent;
                font-size: {StyleManager.get_scaled_font('FONT_SIZE_SETTING')};
                padding: 8px 10px;
                color: {StyleManager.get('TEXT_COLOR_1')};
                border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};
            }}
            
            QListView::item:hover {{
                background-color: {StyleManager.get('MENU_ACTIVE_BG')};
                color: {StyleManager.get('TEXT_COLOR_HOVER')};
                border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};
            }}
            
            QListView::item:selected {{
                background-color: {StyleManager.get('MENU_ACTIVE_BG')};
                color: {StyleManager.get('TEXT_COLOR_HOVER')};
                border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};
            }}
        """)
        
        
    def showPopup(self):
        """
        Override showPopup pour réappliquer le style sur la popup
        à chaque ouverture.
        """
        self._apply_popup_style()
        super().showPopup()