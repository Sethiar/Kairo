from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QSpacerItem
from PyQt6.QtCore import Qt, pyqtSignal

from app.ui.screens.settings.settings_widgets.display_items import LogoDisplayItem
from .menu_button import MenuButton


class MenuWidget(QWidget):

    screenRequested = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(260)
        
        # Background fixe
        self.setStyleSheet("""
            QWidget {
                background-color: #22313F;
            }
        """)

        self.active_button = None
        self._build_ui()
        self._connect_buttons()

    def _build_ui(self):
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(40)
        self.setLayout(self.main_layout)

        # Logo
        self.logo = LogoDisplayItem()
        self.main_layout.addWidget(self.logo, alignment=Qt.AlignmentFlag.AlignTop)
        
        # Petit espacement 
        self.main_layout.addSpacerItem(QSpacerItem(0, 15, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed))
        
        # Boutons
        self.btn_home = MenuButton("Accueil", "screen_home")
        self.btn_start = MenuButton("Planifier une tâche", "screen_tasks")
        self.btn_project = MenuButton("Organiser un projet", "screen_project")
        self.btn_settings = MenuButton("Configuration", "screen_settings")
        self.btn_help = MenuButton("Aide", "screen_help")

        self.buttons = [
            self.btn_home,
            self.btn_start,
            self.btn_project,
            self.btn_settings,
            self.btn_help,
        ]

        for btn in self.buttons:
            self.main_layout.addWidget(btn)

        # Stretch en bas pour pousser les boutons vers le haut
        self.main_layout.addStretch(1)


    def _connect_buttons(self):
        for btn in self.buttons:
            btn.clicked_with_id.connect(self._on_button_clicked)


    def _on_button_clicked(self, target_id: str):
        self._set_active_button(target_id)
        self.screenRequested.emit(target_id)


    def _set_active_button(self, screen_id: str):
        for btn in self.buttons:
            btn.set_active(btn.screen_id == screen_id)

        
        
            