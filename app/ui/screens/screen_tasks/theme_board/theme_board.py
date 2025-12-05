# app.ui/screen/screen_tasks/theme_board/theme_board.py

from PyQt6.QtWidgets import QWidget
from PyQt6.QtCore import pyqtSignal

from app.ui.screens.screen_tasks.theme_board.theme_board_ui import ThemeBoardUI
from app.ui.screens.screen_tasks.theme_column.theme_column import ThemeColumn

class ThemeBoard(QWidget):
    """
    Conteneur principal qui organise toutes les colonnes de thèmes.
    """
    
        
    # Signal pour le controller
    task_clicked = pyqtSignal(dict, object)

    def __init__(self, parent=None):
        super().__init__(parent)
        
        # Déclaration du ThemBoardUi
        self.ui = ThemeBoardUI(self)
        
        # Déclaration du dictionnaire des thèmes
        self.theme_columns = {}

    #-------------------
    # Methodes Utilisateur
    #-------------------
    
    # Reset du tableau
    def clear(self):
        """Efface toutes les colonnes."""
        for column in self.theme_columns.values():
            self.ui.theme_layout.removeWidget(column)
            column.deleteLater()
            
        self.theme_columns.clear()
        
    
    def _get_or_create_column(self, theme_name: str):
        if theme_name not in self.theme_columns:
            col = ThemeColumn(theme_name)
            self.theme_columns[theme_name] = col
            self.ui.theme_layout.addWidget(col)
            
        return self.theme_columns[theme_name]
    
    
    def add_task_to_theme(self, theme_name: str, task_data: dict):
        column = self._get_or_create_column(theme_name)
        card = column.add_task(task_data)

        # Connexion clic -> ThemeBoard
        card.clicked.connect(
            lambda data=task_data, card_widget=card:
                self.task_clicked.emit(data, card_widget)
        )
        
        