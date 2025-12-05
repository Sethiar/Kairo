# app/ui/screens/intro/tuto_panel.py

from PyQt6.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy
from PyQt6.QtCore import Qt, pyqtSignal

from app.assets.assets import LEFT_ARROW_ICON, RIGHT_ARROW_ICON

from .screens import Screen0, Screen1, Screen2, Screen3
from .dot_label import DotLabel 

from app.styles.style_manager import StyleManager

class IntroScreen(QWidget):
    
    """
    Écran d'introduction composé de plusieurs sous-écrans (Screen0..3).

    Fonctionnalités :
    - Navigation via flèches (précédent / suivant)
    - Indicateurs de progression (dots)
    - Empilement des écrans via QStackedWidget
    - Signal `screenChanged` pour notifier le parent du changement d'écran

    Attributs :
        current_index (int): Index du screen actuellement affiché.
        screens (dict[str, QWidget]): Mapping ID → widget de screen.
        dots (list[DotLabel]): Indicateurs visuels pour la progression.
        stack (QStackedWidget): Container principal de screens.
    """
    
    # signal pour le menu ou parent
    screenChanged = pyqtSignal(str)  

    def __init__(self):
        super().__init__()
        
        # Définition des écrans
        self.screens = {
            "screen0": Screen0(self),
            "screen1": Screen1(self),
            "screen2": Screen2(self),
            "screen3": Screen3(self)
        }
        
        self.current_index = 0
        
        # QStackedWidget
        self.stack = QStackedWidget()
        for screen in self.screens.values():
            self.stack.addWidget(screen)

        # Dots (un par screen)
        self.dots = [DotLabel(active=(i==0)) for i in range(len(self.screens))]

        self._build_layout()
        self.show_screen("screen0")
    
    
    # =======================
    # UI CONSTRUCTION
    # ======================= 
    
    def _build_layout(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20,20,20,20)
        
        layout.setSpacing(15)
        self.setLayout(layout)
        

        # Zone centrale avec les écrans 
        self.stack.setSizePolicy(
            QSizePolicy.Policy.Expanding, 
            QSizePolicy.Policy.Expanding
        )
        self.stack.setStyleSheet(f"""
                background: {StyleManager.get('BACKGROUND_COLOR')};
        """)
        layout.addWidget(self.stack)

        # Navigation
        nav_layout = QHBoxLayout()
        self.prev_btn = QPushButton()
        self.prev_btn.setIcon(LEFT_ARROW_ICON)
        self.prev_btn.setFixedSize(50,50)
        self.prev_btn.clicked.connect(self.prev_screen)

        self.next_btn = QPushButton()
        self.next_btn.setIcon(RIGHT_ARROW_ICON)
        self.next_btn.setFixedSize(50,50)
        self.next_btn.clicked.connect(self.next_screen)

        nav_layout.addWidget(self.prev_btn)
        nav_layout.addStretch()
        nav_layout.addWidget(self.next_btn)
        layout.addLayout(nav_layout)

        # Zone dots
        dot_layout = QHBoxLayout()
        dot_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        for dot in self.dots:
            dot_layout.addWidget(dot)
        layout.addLayout(dot_layout)
    
    
    # =======================
    # AFFICHAGE DES ECRANS
    # ======================= 
    
    def show_screen(self, screen_id: str):
        """
        Affiche un screen selon son ID.

        Args:
            screen_id (str): ID du screen à afficher.
        """
        if screen_id not in self.screens:
            print(f"[IntroScreen] screen '{screen_id}' inconnu")
            return
        
        # Mise à jour current index
        self.current_index = list(self.screens.keys()).index(screen_id)
        
        # Changement du widget affiché
        self.stack.setCurrentWidget(self.screens[screen_id])
        
        # Mise à jour visuelle des dots
        for i, dot in enumerate(self.dots):
            dot.set_active(i == self.current_index)
            
            
        # Activation/désactivation des boutons
        max_index = len(self.screens) - 1
        self.prev_btn.setEnabled(self.current_index > 0)
        self.next_btn.setEnabled(self.current_index < max_index)
        
        # Signal vers parent
        self.screenChanged.emit(screen_id)
    
    
    # =======================
    # NAVIGATION ENTRE ECRANS
    # ======================= 
    
    def next_screen(self):
        """Affiche le screen suivant si possible."""
        keys = list(self.screens.keys())
        if self.current_index < len(keys) - 1:
            self.show_screen(keys[self.current_index + 1])
            
    # --------------------------
    
    def prev_screen(self):
        """Affiche le screen précédent si possible."""
        keys = list(self.screens.keys())
        if self.current_index > 0:
            self.show_screen(keys[self.current_index - 1])
            
            