# app/ui/panel/right_panel.py

"""
RightPanel
----------
Conteneur principal pour la partie droite de l’interface.
Affiche dynamiquement l’écran demandé via un QStackedWidget.

Points clés :
    - Style entièrement piloté par StyleManager.
    - Réagit automatiquement aux changements de thème.
    - Construction propre, lisible et extensible.

Auteur : SethiarWorks
Date : 01-01-2026
"""

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QStackedWidget
from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager
from app.ui.screens.intro.tuto_panel import IntroScreen


class RightPanel(QWidget):
    """
    Widget conteneur pour l'affichage des écrans de droite.
    """
    def __init__(self):
        super().__init__()
        
        self._init_ui()
        self._apply_style()
        
        # Mise à jour lorsque le thème change
        ThemeManager.get_instance().theme_changed.connect(self._apply_style)
        
    # =======================
    # UI Construction
    # =======================
    
    def _init_ui(self):
        """Construit l'interface du right panel"""
        
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(40,40,40,40)
        self.main_layout.setSpacing(20)
        self.setLayout(self.main_layout)
        
        # Stack des écrans
        self.stack = QStackedWidget()
        self.main_layout.addWidget(self.stack)
        
        # Déclaration des écrans internes
        self.screens = {
            "intro": IntroScreen()
        }
        
        for screen in self.screens.values():
            self.stack.addWidget(screen)

        self.set_screen("intro")
       
        
    # =======================
    # UI Construction
    # =======================
    
    def _apply_style(self):
        """
        Applique le style du RightPanel selon le thème actif.
        """
        
        self.setStyleSheet(f"""
            background-color: {StyleManager.get('BACKGROUND_COLOR')};
            color: {StyleManager.get('TEXT_COLOR_1')};
            border-radius: {StyleManager.get('BORDER_RADIUS_PANEL')};
        """)


    # =======================
    # Screen management
    # =======================    

    def set_screen(self, screen_id: str):
        """Change l’écran affiché si disponible."""
        if screen_id in self.screens:
            self.stack.setCurrentWidget(self.screens[screen_id])
        else:
            print(f"[RightPanel] Screen '{screen_id}' inconnu")
