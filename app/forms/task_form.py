# app/ui/forms/task_form.py

"""
Module task_form.py

Dialog PyQt6 pour créer une tâche dans le planificateur.
Gère la saisie utilisateur et la création en base de données via create_task.

Auteur : SethiarWorks
Date : 01-01-2026
"""
from typing import Optional

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit, QTextEdit,
    QComboBox, QDateTimeEdit, QPushButton, QMessageBox
)

from PyQt6.QtCore import QDateTime, pyqtSignal

from app.database.base import create_task
from app.database.models.task import TaskStatus, TaskPriority



class TaskForm(QDialog):
    """
    Formulaire de création d'une tâche.

    Signals:
        task_created: émis lorsque la tâche est créée avec succès.
    """
    
    task_created = pyqtSignal()
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Création d'une tâche")
        self.setFixedWidth(400)
        self.window_layout = QVBoxLayout()
        self.setLayout(self.window_layout)
        
        # Titre
        self.window_layout.addWidget(QLabel("Titre"))
        self.title_input = QLineEdit()
        self.window_layout.addWidget(self.title_input)
        
        # Description
        self.window_layout.addWidget(QLabel("Description"))
        self.description_input = QTextEdit()
        self.window_layout.addWidget(self.description_input)
        
        # Statut
        self.window_layout.addWidget(QLabel("Statut"))
        self.statut_input = QComboBox()
        # Les valeurs doivent correspondre aux Enum
        self.statut_input.addItems([s.value for s in TaskStatus])
        self.window_layout.addWidget(self.statut_input)

        # Priorité
        self.window_layout.addWidget(QLabel("Priorité"))
        self.priority_input = QComboBox()
        self.priority_input.addItems([p.value for p in TaskPriority])
        self.window_layout.addWidget(self.priority_input)

        # Deadline
        self.window_layout.addWidget(QLabel("Deadline"))
        self.deadline_input = QDateTimeEdit(QDateTime.currentDateTime())
        self.deadline_input.setCalendarPopup(True)
        self.window_layout.addWidget(self.deadline_input)

        # Bouton créer
        self.submit_btn = QPushButton("Créer la tâche")
        self.submit_btn.clicked.connect(self.submit_task)
        self.window_layout.addWidget(self.submit_btn)
        
        
    def submit_task(self):
        """
        Récupère les données saisies, valide, et crée une tâche en base.
        Émet signal task_created si succès.
        """
        title: str = self.title_input.text().strip()
        description: str = self.description_input.toPlainText().strip()
        status: TaskStatus = TaskStatus(self.statut_input.currentText())
        priority: Optional[TaskPriority] = TaskPriority(self.priority_input.currentText())
        deadline = self.deadline_input.dateTime().toPyDateTime()
        
        if not title or not description:
            QMessageBox.warning(self, "Champs manquants", "Titre ou description requis")
            return
        
        # Création dans la base de données
        create_task(title, description, status, priority, deadline)

        QMessageBox.information(self, "Succès", "La tâche a bien été créée.")
        self.task_created.emit()
        self.close()
        
        