# app/ui/widgets/main_widgets/task_card/priority_badge.py

from PyQt6.QtGui import QColor

def get_priority_color(priority: str) -> QColor:
    """
    Retourne la couleur correspondant à la priorité.
    """ 
    p = priority.lower()
    if p == "urgente":
        return QColor(255, 59, 48)
    elif p == "haute":
        return QColor(255, 149, 0)
    elif p == "moyenne":
        return QColor(255, 204, 0)
    else:
        return QColor(52, 199, 89)
    
    