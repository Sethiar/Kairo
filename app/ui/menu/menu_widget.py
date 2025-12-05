# app/ui/menu/menu_widget.py

"""
Module menu_widget
------------------

Contient la classe MenuWidget, qui représente la colonne latérale gauche
du logiciel. Cette partie comprend l'affichage du logo et les boutons de navigation.

Fonctionnalités :
- Afficher les différentes entrées du menu.
- Gérer le bouton actuellement actif.
- Émettre un signal lorsqu'une section est demandée.

Auteur : SethiarWorks
Date : 01-01-2026
"""
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QSpacerItem
from PyQt6.QtCore import Qt, pyqtSignal

from app.ui.widgets.settings_widgets.display_items import LogoDisplayItem
from .menu_button import MenuButton

from app.styles.style_manager import StyleManager


class MenuWidget(QWidget):
    """
    Widget latéral affichant le menu principal de l'application.

    Ce widget :
        - Affiche le logo de l'application.
        - Affiche une liste de boutons de navigation.
        - Gère l'état actif d'un bouton à la fois.
        - Émet un signal `screenRequested(str)` lorsque l'utilisateur clique sur un bouton.

    Signals:
        screenRequested(str): envoyé lorsqu'un bouton est cliqué.
    """
    
    screenRequested = pyqtSignal(str)

    def __init__(self, parent=None):
        """
        Initialise le menu latéral.

        Args:
            parent (QWidget, optional): widget parent.
        """
        super().__init__(parent)
        self.setFixedWidth(260)
        
        # Style du menu (couleur de fond fixe)
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {StyleManager.get('MENU_BACKGROUND_COLOR')};
            }}
        """)

        self.active_button = None
        
        self._build_ui()
        self._connect_buttons()
    
    
    # =======================
    # UI SETUP
    # ======================= 
    def _build_ui(self):
        """
        Construit toute la structure visuelle du menu.
        """
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(40)
        self.setLayout(self.main_layout)

        # Logo
        self.logo = LogoDisplayItem()
        self.main_layout.addWidget(self.logo, alignment=Qt.AlignmentFlag.AlignTop)
        
        # Petit espacement 
        self.main_layout.addSpacerItem(
            QSpacerItem(0, 15, 
                        QSizePolicy.Policy.Minimum, 
                        QSizePolicy.Policy.Fixed
            )
        )
        
        # Définition des boutons
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
        
        # Ajout dans l'UI
        for btn in self.buttons:
            self.main_layout.addWidget(btn)

        # Stretch en bas pour pousser les boutons vers le haut
        self.main_layout.addStretch(1)
    
    
    # =======================
    # CONNECTIONS
    # ======================= 

    def _connect_buttons(self):
        """
        Connecte le signal des boutons à la fonction interne du widget.
        """
        for btn in self.buttons:
            btn.clicked_with_id.connect(self._on_button_clicked)

    
    # =======================
    # BUTTON HANDLING
    # =======================
    def _on_button_clicked(self, target_id: str):
        """
        Callback appelé lorsqu'un bouton émet son ID.

        Args:
            target_id (str): identifiant de l'écran demandé.
        """
        self._set_active_button(target_id)
        self.screenRequested.emit(target_id)


    def _set_active_button(self, screen_id: str):
        """
        Met à jour l’état actif des boutons du menu.

        Args:
            screen_id (str): ID de l’écran à activer.
        """
        for btn in self.buttons:
            btn.set_active(btn.screen_id == screen_id)

        
        
            