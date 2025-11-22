# app/main_window.py

from PyQt6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QSplitter, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont

from app.styles.style_manager import StyleManager
from app.ui.menu.menu_widget import MenuWidget
from app.ui.screens.screen_manager import ScreenManager
from app.core.settings.theme_manager import ThemeManager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Kairo")
        self.setMinimumSize(1200, 800)

        self.theme_manager = ThemeManager.get_instance()
        self.theme_manager.theme_changed.connect(self.apply_global_theme)

        # -----------------------
        # Central widget
        # -----------------------
        central = QWidget()
        self.setCentralWidget(central)

        layout = QHBoxLayout(central)
        layout.setContentsMargins(0, 0, 0, 0)

        splitter = QSplitter(Qt.Orientation.Horizontal)
        splitter.setHandleWidth(4)
        layout.addWidget(splitter)

        # Menu
        self.menu = MenuWidget()
        splitter.addWidget(self.menu)

        # Screens
        self.screen_manager = ScreenManager()
        splitter.addWidget(self.screen_manager)

        splitter.setSizes([260, 1000])

        # Navigation (menu → screen)
        self.menu.screenRequested.connect(self.screen_manager.switch_to)

        # Initial stylesheet
        self.apply_global_theme()

    # -----------------------
    # Application du thème
    # -----------------------
    def apply_global_theme(self):
        app = QApplication.instance()

        # Police
        family = StyleManager.get("FONT_FAMILY").split(",")[0].strip()
        size = int(str(StyleManager.get("FONT_SIZE_DEFAULT")).replace("px", "").strip())

        font = QFont(family, size)
        app.setFont(font)

        # Background global
        self.setStyleSheet(f"""
            background-color: {StyleManager.get("BACKGROUND_COLOR")};
            color: {StyleManager.get("TEXT_COLOR_1")};
        """)

        self.repaint()
        app.processEvents()