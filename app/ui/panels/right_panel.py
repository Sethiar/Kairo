from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget
from PyQt6.QtCore import Qt
from app.styles.style_manager import StyleManager
from app.ui.screens.intro.tuto_panel import IntroScreen

class RightPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.setObjectName("RightPanel")
        self.setStyleSheet(f"""
            background-color: "#FFFFFF";
            color: #000000;
            border: 2px solid #FFFFFF;
            border-radius: 18px;
        """)

        layout = QVBoxLayout()
        layout.setContentsMargins(40,40,40,40)
        layout.setSpacing(20)
        self.setLayout(layout)

        self.stack = QStackedWidget()
        layout.addWidget(self.stack)

        # Screens internes
        self.screens = {
            "intro": IntroScreen()
        }
        for screen in self.screens.values():
            self.stack.addWidget(screen)

        self.set_screen("intro")

    def set_screen(self, screen_id: str):
        if screen_id in self.screens:
            self.stack.setCurrentWidget(self.screens[screen_id])
        else:
            print(f"[RightPanel] Screen '{screen_id}' inconnu")
