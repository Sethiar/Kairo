from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import pyqtSignal, Qt

from app.styles.style_manager import StyleManager


class MenuButton(QPushButton):
    
    clicked_with_id = pyqtSignal(str)
    
    def __init__(self, text, screen_id, parent=None):
        super().__init__(text, parent)
        self.screen_id = screen_id
        self.active = False

        self._apply_base_style()
        self.clicked.connect(self._emit_id)

    def _emit_id(self):
        self.clicked_with_id.emit(self.screen_id)

    def _apply_base_style(self):
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setStyleSheet(f"""
            QPushButton {{
                padding: 12px 20px;
                border-radius: 10px;
                font-size: {StyleManager.get('FONT_SIZE_BUTTON')};
                font-weight: {StyleManager.get('FONT_WEIGHT_SEMIBOLD')};
                color: {StyleManager.get('MENU_TEXT')};
                background: transparent;
            }}
            QPushButton:hover {{
                background: {StyleManager.get('MENU_HOVER_BG')};
            }}
        """)

    def set_active(self, is_active: bool):
        self.active = is_active
        if is_active:
            self.setStyleSheet(f"""
                QPushButton {{
                    padding: 12px 20px;
                    border-radius: {StyleManager.get('BORDER_RADIUS')};
                    font-size: {StyleManager.get('FONT_SIZE_BUTTON')};
                    font-weight: {StyleManager.get('FONT_WEIGHT_BOLD')};
                    color: {StyleManager.get('TEXT_COLOR_1')};
                    background: {StyleManager.get('MENU_ACTIVE_BG')};
                }}
            """)
        else:
            self._apply_base_style()