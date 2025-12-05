# app/ui/screens/screen_task/controller.py

from PyQt6.QtCore import QObject, pyqtSignal

from app.database.base import get_all_tasks, delete_task, update_task, create_task


class TasksController(QObject):
    """
    Controller pour ScreenTasks.
    - Charge les tâches depuis la DB.
    - Applique tri multi-critères et filtrage.
    - Gère la sélection des cartes.
    """

    task_selected = pyqtSignal(dict)

    def __init__(
        self, 
        theme_board, 
        sort_combobox, 
        search_input=None
    ):
        """
        :param ???
        :param sort_combobox: CustomComboBox pour le tri
        :param search_input: Optional QLineEdit pour filtrage
        """
        super().__init__()
        self.theme_board = theme_board
        self.sort_combobox = sort_combobox
        self.search_input = search_input

        # Connexions
        self.theme_board.task_clicked.connect(self._on_task_clicked)
        
        self.sort_combobox.currentTextChanged.connect(self.reload_tasks)
        if self.search_input:
            self.search_input.textChanged.connect(self.reload_tasks)

    
    # =======================
    # Chargement des tâches
    # =======================
    
    def reload_tasks(self):
        """Charge et trie les tâches selon le critère choisi."""
        tasks = get_all_tasks()
       
        # --- Filtrage par recherche ---
        if self.search_input:
            query = self.search_input.text().strip().lower()
            if query:
                tasks = [
                    t for t in tasks
                    if query in t["theme"].lower() 
                    or query in t["title"].lower() 
                    or query in t["description"].lower()
                ]

        # --- Tri ---
        sort_key = self.sort_combobox.currentText()
        if sort_key == "Date de fin":
            # Trier par deadline croissant
            tasks.sort(key=lambda t: t["deadline"] or "9999-12-31")
        elif sort_key == "Urgence":
            # Trier par priorité : Haute -> Moyenne -> Basse
            priority_order = {"Urgente":0, "Haute": 1, "Moyenne": 2, "Basse": 3}
            tasks.sort(key=lambda t: priority_order.get(t.get("priority", "Moyenne"), 1))
        elif sort_key == "Deadline puis Urgence":
            # Tri combiné : deadline, puis priorité
            priority_order = {"Urgente":0, "Haute": 1, "Moyenne": 2, "Basse": 3}
            tasks.sort(key=lambda t: (t["deadline"] or "9999-12-31", priority_order.get(t.get("priority", "Moyenne"), 1)))

        # Mise à jour UI
        self.theme_board.clear()
        for task in tasks:
            theme = task.get("theme", "Sans titre")
            self.theme_board.add_task_to_theme(task["theme"], task)
    
    
    # =======================
    # Sélection d'une tâche
    # =======================
    
    def _on_task_clicked(self, task_data, card_widget):
        # Désélection de toutes les cartes
        for column in self.theme_board.theme_columns.values():
            for card in column.tasks:
                card.set_selected(False)
        
        #Sélection de la carte cliquée
        card_widget.set_selected(True)
        
        # Emission du signal        
        self.task_selected.emit(task_data)
    
    
    # =======================  
    # Suppression de la tâche
    # =======================
    def suppress_task(self, task_id):
        # Supprime de la DB et recharge la liste
        delete_task(task_id)
        self.reload_tasks()
        
        
    # =======================
    # Modification de la tâche
    # =======================
    def edit_task(self, task_id: int, **kwargs):
        update_task(task_id, **kwargs)
        self.reload_tasks()
        
    
    # =======================
    # Création de la tâche
    # =======================    
    def create_task_from_form(self, data):
        create_task(**data)
        self.reload_tasks()    
        
        