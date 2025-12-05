# app/ui/widgets/main_widgets/task_card/task_card_labels.py

from PyQt6.QtWidgets import QVBoxLayout
from PyQt6.QtCore import Qt

from app.ui.widgets.system.label import SubtitleLabel

class TaskCardLabels:
    """
    Crée et gère les labels d'une TaskCard.
    """
    def __init__(self, task_data):
        self.task_data = task_data
        self.layout = QVBoxLayout()
        self.layout.setSpacing(3)
        self.layout.setContentsMargins(30, 10, 20, 10)
        self._create_labels()

    def _create_labels(self):
        self.title_label = SubtitleLabel(f"Titre : {self.task_data.get('title', 'Sans titre')}")
        self.status_label = SubtitleLabel(f"Statut : {self.task_data.get('status', 'Inconnu')}")
        self.priority_label = SubtitleLabel(f"Priorité : {self.task_data.get('priority', 'moyenne')}")
        
        self.layout.addWidget(self.title_label)
        self.layout.addWidget(self.status_label)
        self.layout.addWidget(self.priority_label)