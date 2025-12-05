from PyQt6.QtWidgets import QScrollArea

from app.styles.style_manager import StyleManager

class CustomScrollArea(QScrollArea):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWidgetResizable(True)
        self.apply_theme()
    
    def apply_theme(self):
        self.setStyleSheet(f"""
            QScrollArea {{
                background-color: {StyleManager.get('SETTINGS_BG_COLOR')};
                border: none;
            }}
            
            QScrollBar:vertical {{
                background: {StyleManager.get('BG_DISABLED_COLOR')};
                width: 15px;
                border-radius: 6px;
            }}
            
            QScrollBar::handle:vertical {{
                background: {StyleManager.get('BTN_SETTING_BG_COLOR')};
                min-height: 30px;
                border-radius: 6px;
            }}
            
            QScrollBar::handle:vertical:hover {{
                background: {StyleManager.get('BTN_SETTING_HOVER_BG_COLOR')};
            }}
            
            QScrollBar:horizontal {{
                background: {StyleManager.get('BG_DISABLED_COLOR')};
                height: 12px;
                border-radius: 6px;
            }}
            
            QScrollBar::handle:horizontal {{
                background: {StyleManager.get('BTN_SETTING_BG_COLOR')};
                min-width: 30px;
                border-radius: 6px;
            }}
            
            QScrollBar::handle:horizontal:hover {{
                background: {StyleManager.get('BTN_SETTING_HOVER_BG_COLOR')};
            }}
            
            QScrollBar::add-line, QScrollBar::sub-line {{
                width: 0px;
                height: 0px;
            }}
        """)