from PyQt6.QtWidgets import QDateTimeEdit
                            

from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager
    


class CustomDateTimeEdit(QDateTimeEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setCalendarPopup(True)
        
        # Application du style
        self.apply_theme()
        # Mise à jour du thème choisi
        ThemeManager.get_instance().theme_changed.connect(self.apply_theme)
        
        # On stylise le calendrier dès maintenant
        self._style_calendar()


    def apply_theme(self):
        self.setStyleSheet(f"""
            QDateTimeEdit {{
                font-size: {StyleManager.get_scaled_font('FONT_SIZE_SETTING')};
                padding: 6px 10px 6px 10px; 
                color:{StyleManager.get('TEXT_COLOR_1')};
                background-color: {StyleManager.get('INPUT_BACKGROUND_COLOR')};
                border: 1px solid {StyleManager.get('BORDER_COLOR')};
                border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};
            }}
            QDateTimeEdit::drop-down {{
                width: 20px;
            }}
        """)


    def _style_calendar(self):
        cal = self.calendarWidget()
        cal.setStyleSheet(f"""
            QCalendarWidget {{
                background-color: {StyleManager.get('INPUT_BACKGROUND_COLOR')};
                color: {StyleManager.get('TEXT_COLOR_1')};
                font-size: {StyleManager.get_scaled_font('FONT_SIZE_SETTING')};
                border: 1px solid {StyleManager.get('BORDER_COLOR')};
            }}
            QCalendarWidget QToolButton {{
                background-color: {StyleManager.get('BACKGROUND_COLOR_COMBO')};
                height: 30px;
                border: none;
            }}
            QCalendarWidget QAbstractItemView {{
                selection-background-color: {StyleManager.get('BG_DISABLED_COLOR')};
                outline: none;
            }}
            QCalendarWidget QAbstractItemView::item:selected {{
                background-color: {StyleManager.get('BG_DISABLED_COLOR')};
                color: {StyleManager.get('TEXT_COLOR_1')};
            }}
            QCalendarWidget QAbstractItemView::item:hover {{
                background-color: {StyleManager.get('BORDER_COLOR')};
            }}
        """)
        
        