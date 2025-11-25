from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt6.QtCore import Qt

from app.core.settings.theme_manager import ThemeManager
from app.styles.style_manager import StyleManager

class CustomMessage(QDialog):
    def __init__(self, parent=None, title="Information", message="Message"):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setFixedSize(350, 180)
        self.setModal(True)
        self.setWindowFlags(
            Qt.WindowType.Dialog |
            Qt.WindowType.CustomizeWindowHint |
            Qt.WindowType.WindowTitleHint
        )
        
        # === Layout ===
        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(15)

        # === Label ===
        label = QLabel(message)
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # === Button ===
        btn_ok = QPushButton("OK")
        btn_ok.clicked.connect(self.accept)

        # Ajout au layout
        layout.addWidget(label)
        layout.addWidget(btn_ok, alignment=Qt.AlignmentFlag.AlignCenter)

        # === Style dynamique selon theme ===
        self.apply_theme()

    def apply_theme(self):
  
        bg = StyleManager.get("SETTINGS_BG_COLOR")
        fg = StyleManager.get("TEXT_COLOR_1")
        btn_bg = StyleManager.get("BTN_SETTING_BG_COLOR")
        btn_hover = StyleManager.get("BTN_SETTING_HOVER_BG_COLOR")

        self.setStyleSheet(f"""
            QDialog {{
                background-color: {bg};
                border-radius: 12px;
            }}

            QLabel {{
                color: {fg};
                font-size: 16px;
                font-family: Lato;
            }}

            QPushButton {{
                background-color: {btn_bg};
                color: white;
                padding: 8px 20px;
                border-radius: 8px;
            }}

            QPushButton:hover {{
                background-color: {btn_hover};
            }}
        """)