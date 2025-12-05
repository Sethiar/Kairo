# app/ui/forms/task_form.py

"""
Module task_form.py

Dialog PyQt6 pour créer une tâche dans le planificateur.
Gère la saisie utilisateur et la création en base de données via create_task.

Auteur : SethiarWorks
Date : 01-01-2026
"""
from typing import Optional
from datetime import datetime

from PyQt6.QtWidgets import QVBoxLayout, QMessageBox

from PyQt6.QtCore import QDateTime, pyqtSignal

from app.ui.widgets.system.hover_button import HoverButton
from app.ui.widgets.system.line_edit import CustomLineEdit
from app.ui.widgets.system.text_edit import CustomTextEdit
from app.ui.widgets.system.combo import CustomComboBox
from app.ui.widgets.system.datetime_edit import CustomDateTimeEdit
from app.ui.widgets.system.label import CustomLabel

from app.ui.widgets.main_widgets.main_QDialog import MainDialogForm
 

from app.database.models.task import TaskStatus, TaskPriority



class TaskForm(MainDialogForm):
    """
    Formulaire de création d'une tâche.

    Signals:
        task_created: émis lorsque la tâche est créée avec succès.
    """
    
    task_saved = pyqtSignal(dict)
    
    def __init__(self, parent=None, task_data: Optional[dict] = None):
        super().__init__(parent)
        self.task_data = task_data
        
        self.setWindowTitle("Création d'une tâche" if not task_data else "Modifier la tâche")
        self.setFixedWidth(400)
        self.window_layout = QVBoxLayout()
        self.setLayout(self.window_layout)
        
        # Theme
        self.window_layout.addWidget(CustomLabel("Thème"))
        self.theme_input = CustomLineEdit()
        self.window_layout.addWidget(self.theme_input)
        
        # Titre
        self.window_layout.addWidget(CustomLabel("Titre"))
        self.title_input = CustomLineEdit()
        self.window_layout.addWidget(self.title_input)
        
        # Description
        self.window_layout.addWidget(CustomLabel("Description"))
        self.description_input = CustomTextEdit()
        self.window_layout.addWidget(self.description_input)
        
        # Statut
        self.window_layout.addWidget(CustomLabel("Statut"))
        self.statut_input = CustomComboBox()
        # Les valeurs doivent correspondre aux Enum
        self.statut_input.addItems([s.value for s in TaskStatus])
        self.window_layout.addWidget(self.statut_input)

        # Priorité
        self.window_layout.addWidget(CustomLabel("Priorité"))
        self.priority_input = CustomComboBox()
        self.priority_input.addItems([p.value for p in TaskPriority])
        self.window_layout.addWidget(self.priority_input)

        # Deadline
        label_deadline = CustomLabel("Deadline")
        self.window_layout.addWidget(label_deadline)

        self.deadline_input = CustomDateTimeEdit(self)
        self.deadline_input.setDateTime(QDateTime.currentDateTime())

        self.window_layout.addWidget(self.deadline_input)
        self.window_layout.addSpacing(20)

        # Bouton créer
        self.submit_btn = HoverButton("Créer la tâche" if not task_data else "Modifier la tâche")
        self.submit_btn.clicked.connect(self.submit_task)
        self.window_layout.addWidget(self.submit_btn)
        
        
         # --- Préremplir si édition ---
        if task_data:
            self._fill_form(task_data)
        
    def _fill_form(self, task_data: dict):
        """
        Pré-remplit lel formulaire pour l'édition
        """
        self.theme_input.setText(task_data.get("theme",""))
        self.title_input.setText(task_data.get("title", ""))
        self.description_input.setText(task_data.get("description", ""))
        self.statut_input.setCurrentText(task_data.get("status", TaskStatus.A_FAIRE.value))
        self.priority_input.setCurrentText(task_data.get("priority", TaskPriority.MOYENNE.value))
        
        deadline = task_data.get("deadline")
        if deadline:
            # convertir ISO string -> datetime -> QDateTime
            if isinstance(deadline, str):
                dt = datetime.fromisoformat(deadline)
            else:
                dt = deadline
            self.deadline_input.setDateTime(QDateTime(dt))
            
                
    def submit_task(self):
        """
        Récupère les données saisies, valide, et crée une tâche en base.
        Émet signal task_created si succès.
        """
        theme: str = self.theme_input.text().strip()
        title: str = self.title_input.text().strip()
        description: str = self.description_input.toPlainText().strip()
        status_enum = TaskStatus(self.statut_input.currentText())
        priority_enum = TaskPriority(self.priority_input.currentText()) if self.priority_input.currentText() else None
        deadline = self.deadline_input.dateTime().toPyDateTime()
        
        if not title or not description:
            QMessageBox.warning(self, "Champs manquants", "Titre ou description requis")
            return
        
        data = {
            "theme": theme,
            "title": title,
            "description": description,
            "status": status_enum,
            "priority": priority_enum,
            "deadline": deadline
        }
        
        if self.task_data:  # édition
            data["id"] = self.task_data["id"]

        self.task_saved.emit(data)
        self.accept()
        
        
        