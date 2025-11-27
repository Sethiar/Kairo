from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout
from PyQt6.QtCore import Qt, pyqtSignal

from app.forms.task_form import TaskForm
from app.database.base import get_all_tasks

# UI
from app.ui.screens.base_screen import BaseScreen
from app.ui.widgets.settings_widgets.hover_label import HoverLabel
from app.ui.widgets.settings_widgets.title_label import TitleLabel
from app.ui.widgets.settings_widgets.separator_widgets import CustomSeparator
from app.ui.widgets.settings_widgets.custom_widgets import CustomComboBox

from app.ui.widgets.main_widgets.subtitle_main_label import SubtitleMainLabel
from app.ui.screens.screen_tasks.task_list_widget import TaskListWidget


class ScreenTasks(BaseScreen):
    task_selected = pyqtSignal(dict)
    
    def __init__(self, scroll=True):
        super().__init__(scroll)
        self.setStyleSheet("background: transparent;")
        
        self.selected_card = None
        
        self._build_ui()
        self.reload_tasks()
        
        
    #------------------------
    # UI CONSTRUCTION
    #------------------------
    def _build_ui(self):
            
        self._init_title()
        
        # ------------------------
        # Layout horizontal principal
        # ------------------------
        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(50, 0, 50, 0)
        self.main_layout.setSpacing(20)
        
        self.inner_layout.addLayout(self.main_layout)
        
        # Colonne gauche
        self._init_left_panel()

        # Colonne droite
        self._init_right_panel()    
   
    
    # ---------------------
    # TITRE + SEPARATEUR
    # ---------------------
    def _init_title(self):
        title_label = TitleLabel('Planification de tâches')
        self.outer_layout.addWidget(title_label)
        
        separator = CustomSeparator()
        self.outer_layout.addWidget(separator)
        self.outer_layout.addSpacing(15)
    
    
    #----------------------
    # PANNEAU GAUCHE
    #----------------------
    def _init_left_panel(self):
        self.left_panel = QVBoxLayout()
        self.left_panel.setSpacing(15)
        self.main_layout.addLayout(self.left_panel, 1)
        
        # Trier par 
        self.left_panel.addWidget(SubtitleMainLabel('Trier par :'))
        
        self.combo_sort = CustomComboBox()
        self.combo_sort.addItems(['Date de fin', 'Urgence'])    
        self.left_panel.addWidget(self.combo_sort)
        
        # Bouton : Ajouter une tâche
        self.btn_add_task = HoverLabel('Ajouter une tâche')
        self.btn_add_task.clicked.connect(self.open_task_form)
        self.left_panel.addWidget(self.btn_add_task)
        
        # Bouton : Modifier une tâche
        self.btn_edit_task = HoverLabel('Modifier la tâche')
        self.btn_edit_task.setEnabled(False)
        self.left_panel.addWidget(self.btn_edit_task)
        
        # Séparateur
        separator = CustomSeparator()
        self.left_panel.addWidget(separator)
        
        # Bouton Paramètres tâches
        self.btn_task_settings = HoverLabel('Paramètres des tâches')
        self.left_panel.addWidget(self.btn_task_settings)

        # Bouton Calendrier
        self.btn_calendar = HoverLabel('Calendrier')
        self.left_panel.addWidget(self.btn_calendar)
        
        
    #----------------------
    # PANNEAU DROIT
    #----------------------
    def _init_right_panel(self):
        self.right_panel =QVBoxLayout()
        self.right_panel.setSpacing(20)
        self.main_layout.addLayout(self.right_panel, 3)
        
        title = TitleLabel('Tableau des tâches')
        self.right_panel.addWidget(title)
        
        separator = CustomSeparator()
        self.right_panel.addWidget(separator)
        self.right_panel.addSpacing(10)
        
        
        # Widget qui gère les cartes
        self.list_widget = TaskListWidget()
        self.list_widget.card_clicked.connect(self.on_task_clicked)
        self.right_panel.addWidget(self.list_widget)
        
        
    #----------------------------
    # Formulaire
    #---------------------------- 
    def open_task_form(self):
        form = TaskForm()
        # Connexion au signal
        form.task_created.connect(self.reload_tasks)
        form.setModal(True)
        form.exec()
        form.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)   
        
            
    # ---------------------
    # Chargement des tâches
    # ---------------------
    def reload_tasks(self):
        tasks = get_all_tasks()
        self.list_widget.populate(tasks)

        # Désactiver "Modifier" tant qu'aucune carte sélectionnée
        self.btn_edit_task.setEnabled(False)
        self.selected_card = None
            
    
    #-----------------------
    # Sélection d'une tâche
    #-----------------------
    def on_task_clicked(self, task_data, card_widget):
        
        # Désélectionner ancienne carte
        if self.selected_card:
            self.selected_card.set_selected(False)
            
        # Sélectiononer nouvelle carte
        self.selected_card = card_widget
        self.selected_card.set_selected(True)
        
        # Activer bouton modifier
        self.btn_edit_task.setEnabled(True)
        
        # Propagation de l'événement
        self.task_selected.emit(task_data)
        
           