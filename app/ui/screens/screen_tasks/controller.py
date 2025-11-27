
from PyQt6.QtCore import QObject, pyqtSignal


from app.forms.task_form import TaskForm
from app.ui.widgets.main_widgets.taskcard_widget import TaskCard

from app.database.base import get_all_tasks


class TasksController(QObject):
    task_selected = pyqtSignal(dict)
    
    def __init__(self, list_widget):
        super().__init__()
        self.list_widget = list_widget
        self.list_widget.card_clicked.connect(self.on_card_clicked)
        
            
    def on_card_clicked(self, task_data):
        self.task_selected.emit(task_data)  
        
        

          