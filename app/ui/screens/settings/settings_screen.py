# app/ui/screens/settings/settings_screen.py

from app.ui.screens.settings.base_settings_screen import BaseSettingsScreen
from app.ui.screens.settings.sections.user_section import UserSection
from app.ui.screens.settings.sections.appearence_section import AppearanceSection
from app.ui.screens.settings.sections.music_section import MusicSection


class SettingsScreen(BaseSettingsScreen):
    """
    Écran principal des paramètres.
    Hérite directement de BaseSettingsScreen (scroll + layout + sections).
    """
    def __init__(self):
        super().__init__()

        # Ajouter les sections
        self.add_section(UserSection())
        self.add_section(AppearanceSection())
        self.add_section(MusicSection())