# app/ui/screens/screen_manager.py

from PyQt6.QtWidgets import QStackedWidget

from app.ui.panels.right_panel import RightPanel
from app.ui.screens.settings.settings_screen import SettingsScreen
from app.ui.screens.screen_tasks.screen_tasks import ScreenTasks


class ScreenManager(QStackedWidget):
    """
    Gère le changement d'écran proprement
    """

    def __init__(self):
        super().__init__()

        # Instanciation des écrans
        self.screens = {
            "screen_home": RightPanel(),
            "screen_settings": SettingsScreen(),
            "screen_tasks": ScreenTasks(),
        }

        # Ajout au stack
        for screen in self.screens.values():
            self.addWidget(screen)

        # Défaut : écran Dashboard
        self.switch_to("screen_home")

    def switch_to(self, screen_name: str):
        if screen_name not in self.screens:
            print(f"[ScreenManager] Écran inconnu : {screen_name}")
            return

        widget = self.screens[screen_name]
        self.setCurrentWidget(widget)