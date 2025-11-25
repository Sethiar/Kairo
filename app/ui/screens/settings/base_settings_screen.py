# app/ui/screens/settings/base_settings_screen.py

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import Qt

from app.ui.widgets.settings_widgets.notification_widget import CustomMessage
from app.ui.screens.base_screen import BaseScreen
from app.ui.widgets.settings_widgets.hover_button import HoverButton


class BaseSettingsScreen(BaseScreen):
    """
    Base pour l'écran des Paramètres
    - Hérite de BaseScreen
    - Sections + bouton de sauvegarde
    """

    def __init__(self):
        super().__init__(scroll=True)

        self.sections = []

        # Bouton global de sauvegarde
        self.save_btn = HoverButton(
            "Sauvegarder les paramètres",
            width=250,
            height=40
        )
        self.save_btn.clicked.connect(self.save_all_sections)

        self.inner_layout.addWidget(self.save_btn, alignment=Qt.AlignmentFlag.AlignRight)

    # Ajouter une section
    def add_section(self, section_widget: QWidget):
        self.inner_layout.insertWidget(self.inner_layout.count() - 1, section_widget)
        self.sections.append(section_widget)

    # Sauvegarde globale
    def save_all_sections(self):
        for section in self.sections:
            if hasattr(section, "on_save"):
                section.on_save()

        popup = CustomMessage(self, "Paramètres", "Les paramètres ont bien été sauvegardés.")
        popup.exec()