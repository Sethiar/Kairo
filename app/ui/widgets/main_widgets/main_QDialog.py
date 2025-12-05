# app/ui/widget/main_widget/main_QDialog.py
"""
Fichier de base pour la fenêtre QDialog de l'application

Ce fichier prendra en charge tous les styles des fenêtres QDialog ouvertes par l'utilisateur.

"""


from PyQt6.QtWidgets import QDialog


from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager


class MainDialogForm(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self._apply_theme()
        
        ThemeManager.get_instance().theme_changed.connect(self._apply_theme)
        
    def _apply_theme(self):
        self.setStyleSheet(f"""
            background: {StyleManager.get('BACKGROUND_COLOR')};
        """)
        
        


