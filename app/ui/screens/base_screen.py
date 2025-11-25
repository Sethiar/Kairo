# app/ui/screens/base_screen.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QScrollArea
from PyQt6.QtCore import Qt

from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager


class BaseScreen(QWidget):
    """
    Base commune pour TOUS les écrans.
    - Background cohérent avec le thème
    - Layout vertical prêt à l’emploi
    - Scroll optionnel
    """

    def __init__(self, scroll=False):
        super().__init__()
        self.outer_layout = QVBoxLayout(self)
        self.outer_layout.setContentsMargins(0, 0, 0, 0)
        
        # --------------------------
        # MODE AVEC SCROLL
        # --------------------------
        if scroll:

            scroll_area = QScrollArea()
            scroll_area.setWidgetResizable(True)
             
            self.inner_widget = QWidget()
            scroll_area.setWidget(self.inner_widget)
            
            self.inner_layout = QVBoxLayout(self.inner_widget)
            
            self.outer_layout.addWidget(scroll_area)

        else:
            self.inner_widget = self
            self.inner_layout = QVBoxLayout(self)
            
        # Thème appliqué ici
        self.apply_theme()    
        
        # Mise à jour dynamique
        ThemeManager.get_instance().theme_changed.connect(self.apply_theme)
        
    
    def apply_theme(self):
        """Applique le thème au fond de tous les écrans."""
        self.setStyleSheet(f"""
            QWidget {{
                background-color: {StyleManager.get('SETTINGS_BG_COLOR')};
            }}
        """)
        
        