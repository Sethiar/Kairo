# app/ui/screens/base_screen.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt

from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager

from app.ui.widgets.system.scroll_widget import CustomScrollArea
class BaseScreen(QWidget):
    """
    Base commune pour TOUS les écrans.
    - Background cohérent avec le thème
    - Layout vertical prêt à l’emploi
    - Scroll optionnel
    """

    def __init__(self, scroll=False):
        super().__init__()
        
        self.setProperty("class", "base-screen")
        
        self.outer_layout = QVBoxLayout(self)
        self.outer_layout.setContentsMargins(0, 0, 0, 0)
        
        # --------------------------
        # MODE AVEC SCROLL
        # --------------------------
        if scroll:

            scroll_area = CustomScrollArea()
            scroll_area.setWidgetResizable(True)
             
            self.inner_widget = QWidget()
            scroll_area.setWidget(self.inner_widget)
            
            self.inner_layout = QVBoxLayout(self.inner_widget)
            
            self.outer_layout.addWidget(scroll_area)

        else:
            self.inner_widget = self
            self.inner_layout = QVBoxLayout(self)
             
   