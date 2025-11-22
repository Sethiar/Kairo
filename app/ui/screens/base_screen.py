# app/ui/screens/base_screen.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt

from app.styles.style_manager import StyleManager


class BaseScreen(QWidget):
    """
    Base commune pour TOUS les écrans.
    - Background cohérent avec le thème
    - Layout vertical prêt à l’emploi
    - Scroll optionnel
    """

    def __init__(self, scroll: bool = False):
        super().__init__()

        # Application du style global pour tous les écrans
        self.setStyleSheet(f"""
            background-color: {StyleManager.get("SETTINGS_BG_COLOR")};
            color: {StyleManager.get("TEXT_COLOR_2")};
        """)

        if scroll:
            # --------------------------
            # MODE AVEC SCROLL
            # --------------------------
            self.outer_layout = QVBoxLayout(self)
            self.outer_layout.setContentsMargins(0, 0, 0, 0)

            self.scroll_area = QScrollArea()
            self.scroll_area.setWidgetResizable(True)
            self.scroll_area.setFrameShape(QScrollArea.Shape.NoFrame)
            self.scroll_area.setStyleSheet("border: none;")

            self.container = QWidget()
            self.layout = QVBoxLayout(self.container)
            self.layout.setContentsMargins(20, 20, 20, 20)

            self.scroll_area.setWidget(self.container)
            self.outer_layout.addWidget(self.scroll_area)
        else:
            # --------------------------
            # MODE SANS SCROLL (simple)
            # --------------------------
            self.layout = QVBoxLayout(self)
            self.layout.setContentsMargins(20, 20, 20, 20)