from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import pyqtSignal

from app.ui.widgets.main_widgets.taskcard_widget import TaskCard


class TaskListWidget(QWidget):
    card_clicked = pyqtSignal(dict, object)
    
    def __init__(self):
        super().__init__()
        self.list_layout = QVBoxLayout(self)
        self.list_layout.setSpacing(15)
        
        self.cards = []
        
    def populate(self, tasks):
        # Clear
        for card in self.cards:
            card.deleteLater()
        
        self.cards.clear()
        
        # Add
        for task_data in tasks:
            card = TaskCard(task_data)
            card.clicked.connect(
                lambda data=task_data, c=card: self.card_clicked.emit(data, c)
            )
            
            self.list_layout.addWidget(card)
            self.cards.append(card)                     
        
        self.list_layout.addStretch(1)
         
    def select_card(self, card):
        for c in self.cards:
            c.set_selected(False)
        card.set_selected(True)
        
            