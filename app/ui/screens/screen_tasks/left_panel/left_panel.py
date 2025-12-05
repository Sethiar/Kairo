# app/screen/screen_task/left_panel/left_panel.py

from PyQt6.QtWidgets import QVBoxLayout

# UI
from app.ui.screens.base_screen import BaseScreen
from app.ui.screens.screen_tasks.controller import TasksController

from app.ui.widgets.system.hover_button import HoverButton
from app.ui.widgets.system.combo import CustomComboBox
from app.ui.widgets.system.line_edit import CustomLineEdit
from app.ui.widgets.system.label import SubtitleLabel


class ScreenTaskLeftPanel(BaseScreen):
    """
    Docstring pour ScreenTaskLeftPanel
    
    
    """
    def __init__(self, scroll=False):
        super().__init__(scroll)
        
        self.selected_task = None
        
        self._build_ui()
        
    
    #--------------------------    
    # UI CONSTRUCTION    
    #-------------------------- 
    def _build_ui(self):
        
        # Layout horizontal principal
        left_panel_layout = QVBoxLayout()
        left_panel_layout.addSpacing(20)
        left_panel_layout.setContentsMargins(20, 20, 20, 20)
        
        #--------------------
        # Boutons d'action
        #--------------------
        
        # Recherche
        self.search_input = CustomLineEdit()
        self.search_input.setPlaceholderText("Titre ou description")
        left_panel_layout.addWidget(SubtitleLabel("Rechercher"))
       
        # Tri
        self.combo_sort = CustomComboBox()
        self.combo_sort.addItems(['Date de fin', 'Urgence', 'Deadline puis Urgence'])
        
        # Ajout de tâches
        self.btn_add = HoverButton("AJouter une tâche")
        self.btn_add.setObjectName("ActionButton")
        
        # Modification de la tâche sélectionnée
        self.btn_edit = HoverButton("Modifier une tâche")
        self.btn_edit.setObjectName("ActionButton")
        
        # Suppression de la tâche sélectionnée
        self.btn_delete = HoverButton("Supprimer une tâche")
        self.btn_delete.setObjectName("ActionButton")

        
        # Ajout dans le layout
        left_panel_layout.addWidget(self.search_input)
        left_panel_layout.addSpacing(15)
        
        left_panel_layout.addWidget(self.combo_sort)
        left_panel_layout.addSpacing(15)
        
        left_panel_layout.addWidget(self.btn_add)
        left_panel_layout.addSpacing(15)
        
        left_panel_layout.addWidget(self.btn_edit)
        left_panel_layout.addSpacing(15)
        
        left_panel_layout.addWidget(self.btn_delete)
        left_panel_layout.addSpacing(15)
        
        left_panel_layout.addStretch(1)
        
        self.inner_layout.addLayout(left_panel_layout)
        