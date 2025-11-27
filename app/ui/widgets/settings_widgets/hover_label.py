
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import  QEnterEvent
from PyQt6.QtCore import Qt


from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager

class HoverLabel(QPushButton):
    """Bouton avec hover couleur simple et propre."""

    def __init__(self, text="", width=120, height=40):
        super().__init__(text)

        self.setFixedSize(width, height)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.apply_theme()
        ThemeManager.get_instance().theme_changed.connect(self.apply_theme)
        
        
    def apply_theme(self):
        self.default_bg = StyleManager.get("BTN_SETTING_BG_COLOR")
        self.hover_bg = StyleManager.get("BTN_SETTING_HOVER_BG_COLOR")
        self.default_fg = StyleManager.get("BUTTON_FG")
        self.hover_fg = StyleManager.get("BUTTON_FG_HOVER")
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.default_bg};
                color: {self.default_fg};
                border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};
                font-size: {StyleManager.get('FONT_SIZE_SETTING')};
            }}
        """)

    def enterEvent(self, event):
        self.setStyleSheet(f"""
            QPushButton {{
                background-color: {self.hover_bg};
                color: {self.hover_fg};
                border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};
                font-size: {StyleManager.get('FONT_SIZE_SETTING')};
            }}
        """)
        super().enterEvent(event)

    def leaveEvent(self, event: QEnterEvent):
        self.apply_theme()
        super().leaveEvent(event)