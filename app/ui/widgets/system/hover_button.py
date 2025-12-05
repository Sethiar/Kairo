from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import Qt

from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager



class HoverButton(QPushButton):
    def __init__(self, text="", width=150, height=40):
        super().__init__(text)
        self.setFixedSize(width, height)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.apply_theme()
        ThemeManager.get_instance().theme_changed.connect(self.apply_theme)

    def apply_theme(self):
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {StyleManager.get("BTN_SETTING_BG_COLOR")};
                color: {StyleManager.get("BUTTON_FG")};
                border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};
                font-size: {StyleManager.get_scaled_font('FONT_SIZE_SETTING')};
            }}
        """)

    def enterEvent(self, event):
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {StyleManager.get("BTN_SETTING_HOVER_BG_COLOR")};
                color: {StyleManager.get("BTN_SETTING_BG_COLOR")};
                border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};
                font-size: {StyleManager.get_scaled_font('FONT_SIZE_SETTING')};
            }}
        """)
        
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.apply_theme()
        super().leaveEvent(event)