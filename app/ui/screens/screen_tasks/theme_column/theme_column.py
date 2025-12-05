# app/ui/screens/screen_task/theme_column/theme_column_ui.py

from PyQt6.QtWidgets import QWidget, QVBoxLayout

from app.ui.screens.screen_tasks.theme_column.theme_column_ui import ThemeColumnUI

from app.ui.widgets.main_widgets.task_card.task_card import TaskCard


class ThemeColumn(QWidget):
    """
    Colonne d'un thème :
    - Titre du thème
    - Cartes associées
    """
    
    def __init__(self, theme_name: str, parent=None):
        super().__init__(parent)
        
        self.theme_name = theme_name
        
        self.ui = ThemeColumnUI(theme_name)
        
        self.tasks = []
        
        layout = QVBoxLayout()
        layout.addWidget(self.ui)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
        
        
    #-------------------
    # Methodes Utilisateur
    #-------------------   
    def add_task(self, task_data: dict):
        card = TaskCard(task_data)
        self.tasks.append(card)
        
        self.ui.tasks_layout.addWidget(card)
        
        return card
        