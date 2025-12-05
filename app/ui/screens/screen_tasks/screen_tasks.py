# app/ui/screens/screen_tasks/screen_tasks.py

from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QMessageBox
from PyQt6.QtCore import Qt, pyqtSignal

# UI
from app.ui.screens.base_screen import BaseScreen
from app.ui.screens.screen_tasks.theme_board.theme_board import ThemeBoard

from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager
from app.ui.screens.screen_tasks.left_panel.left_panel import ScreenTaskLeftPanel
from app.ui.widgets.system.label import TitleLabel
from app.ui.widgets.system.separator import CustomSeparator

from .controller import TasksController
from app.forms.task_form import TaskForm



class ScreenTasks(BaseScreen):
    """
    Screen principal pour gérer les tâches :
    - Liste de tâches avec TaskListWidget
    - Tri via CustomComboBox
    - Recherche via QLineEdit
    - Ajout et modification des tâches
    """
    
    task_selected = pyqtSignal(dict)

    def __init__(self, scroll=True):
        super().__init__(scroll)
        
        self.setObjectName("ScreenTasks")
        
        self.selected_task = None
        
        self._build_ui()
        self._init_controller()
        
        # Application du style
        self.apply_theme()
          
        # Mise à jour dynamique
        ThemeManager.get_instance().theme_changed.connect(self.apply_theme)

     
    # =======================
    # UI CONSTRUCTION
    # =======================
    def _build_ui(self):
            
        # Layout horizontal principal
        self.main_layout = QHBoxLayout()
        self.main_layout.setContentsMargins(50, 0, 50, 0)
        self.main_layout.setSpacing(20)
        self.inner_layout.addLayout(self.main_layout)
        
        # Colonne gauche
        self.left_panel = ScreenTaskLeftPanel(scroll=False)
        self.main_layout.addLayout(self.left_panel.inner_layout, 1)
        
        # Connexions des boutons
        self.left_panel.btn_add.clicked.connect(self.open_task_form)
        self.left_panel.btn_edit.clicked.connect(self.edit_selected_task)
        self.left_panel.btn_delete.clicked.connect(self.delete_selected_task)
        
        # Colonne droite
        self.right_panel = QVBoxLayout()
        
        
        title = TitleLabel("Tableau des tâches")
        self.right_panel.addWidget(title)
        
        separator = CustomSeparator()
        self.right_panel.addWidget(separator)
        self.right_panel.addSpacing(10)
        
        
        # Insertion du tableau des thèmes 
        self.theme_board = ThemeBoard()
        self.right_panel.addWidget(self.theme_board)
        self.right_panel.setStretchFactor(self.theme_board, 1)
        
        # Mise en place au 3/4 de l'écran
        self.main_layout.addLayout(self.right_panel, 3)
        
        self.right_panel.addStretch(0)
        
    # =======================
    # Controller
    # =======================
    def _init_controller(self):
        self.controller = TasksController(
            theme_board=self.theme_board,
            sort_combobox=self.left_panel.combo_sort,
            search_input=self.left_panel.search_input
        )
        self.controller.task_selected.connect(self._on_task_selected)
        
        # Premier chargement
        self.controller.reload_tasks()    
        
        
    # =======================
    # Styles
    # =======================    
    def apply_theme(self):
        self.setStyleSheet(f"""
            ScreenTasks {{
                font-size: {StyleManager.get_scaled_font('FONT_SIZE_SETTING')};
                background-color: {StyleManager.get('MAIN_BG_COLOR')};
                border-radius: {StyleManager.get('BORDER_RADIUS')};
            }}
        """)    
    
    
    # =======================
    # UI handlers
    # =======================
    # Sélection d'une carte
    def _on_task_selected(self, task_data):
        self.selected_task = task_data
        self.left_panel.btn_edit.setEnabled(True)
        self.left_panel.btn_delete.setEnabled(True)
        self.task_selected.emit(task_data)
        
        
    # Ajout de la modification
    def update_task_selection(self, tasks):
        """Après rechargement des tâches, désélectionner tout."""
        self.selected_task = None
        self.left_panel.btn_edit.setEnabled(False)
        self.left_panel.btn_delete.setEnabled(False)    
        
        
    # Ouverture du formulaire  
    def open_task_form(self):
        """Ouvre le formulaire de création de nouvelle tâche."""
        form = TaskForm()
        
        # Connexion au signal
        form.task_saved.connect(lambda data: self.controller.create_task_from_form(data))
        form.setModal(True)
        form.exec()
        form.setAttribute(Qt.WidgetAttribute.WA_DeleteOnClose)  
        
        
    # Modification sur carte
    def edit_selected_task(self):
        if not self.selected_task:
            return
        form = TaskForm(task_data=self.selected_task)
        form.task_saved.connect(lambda data: self.controller.edit_task(data.pop("id"), **data))
        form.setModal(True)
        form.exec() 
      
        
    # Message de confirmation
    def delete_selected_task(self):
        if not self.selected_task:
            return
        reply = QMessageBox.question(
            self,
            "Confirmer la suppression",
            "Êtes-vous sûr·e de vouloir supprimer cette tâche ?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if reply == QMessageBox.StandardButton.Yes:
            self.controller.suppress_task(self.selected_task["id"])           
    
    
