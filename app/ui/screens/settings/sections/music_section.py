from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame
from PyQt6.QtCore import Qt

from app.ui.screens.settings.settings_widgets.music_widgets import MusicWidget
from app.ui.screens.settings.settings_widgets.separator_widgets import CustomSeparator
from app.ui.screens.settings.settings_widgets.title_label import TitleLabel

class MusicSection(QWidget):
    """Section wrapper (titre + séparateur + widget music)."""
    def __init__(self):
        super().__init__()
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(30, 10, 30, 20)
        self.main_layout.setSpacing(12)
        self.setLayout(self.main_layout)

        title = TitleLabel("Paramètres de la bibliothèque musicale")
        self.main_layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignTop)

        separator = CustomSeparator()
        self.main_layout.addWidget(separator)
        self.main_layout.addSpacing(12)

        # Le widget qui contient la liste + boutons + preview
        self.music_widget = MusicWidget()
        self.main_layout.addWidget(self.music_widget)   
