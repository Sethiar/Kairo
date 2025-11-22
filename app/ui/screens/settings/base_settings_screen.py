# app/ui/screens/settings/base_settings_screen.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt

from app.ui.screens.base_screen import BaseScreen
from app.styles.style_manager import StyleManager
from app.ui.screens.settings.settings_widgets.hover_button import HoverButton


class BaseSettingsScreen(BaseScreen):
    """
    Base pour l'écran des Paramètres
    - Hérite de BaseScreen
    - Scroll inclus automatiquement
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

        self.layout.addWidget(self.save_btn, alignment=Qt.AlignmentFlag.AlignRight)

    # Ajouter une section
    def add_section(self, section_widget: QWidget):
        self.layout.insertWidget(self.layout.count() - 1, section_widget)
        self.sections.append(section_widget)

    # Sauvegarde globale
    def save_all_sections(self):
        for section in self.sections:
            if hasattr(section, "on_save"):
                section.on_save()

        msg = QMessageBox(self)
        msg.setWindowTitle("Paramètres")
        msg.setText("Les paramètres ont bien été sauvegardés.")
        msg.exec()