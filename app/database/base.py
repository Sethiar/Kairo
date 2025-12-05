# app/database/base.py

"""
Module base.py

Fonctions utilitaires pour la gestion des tâches :
- création
- récupération
- sérialisation
Gestion de session SQLAlchemy et typage complet.


Auteur : SethiarWorks
Date : 01-01-2026
"""

from datetime import datetime
from typing import List, Optional, Dict, Any

from app.database.engine import SessionLocal
from app.database.models.task import Task, TaskStatus, TaskPriority


# =======================
# Création d'une tâche
# =======================r
def create_task(
    
    theme: str, title: str, description: str,
    status: TaskStatus = TaskStatus.A_FAIRE,
    priority: Optional[TaskPriority] = None,
    deadline: Optional[datetime] = None
) -> Task:
    """
    Crée une nouvelle tâche et la sauvegarde en base de données.

    Args:
        theme (str): Thème de la tâche
        title (str): Titre de la tâche
        description (str): Description détaillée
        status (TaskStatus, optional): Statut de la tâche
        priority (TaskPriority, optional): Priorité
        deadline (datetime, optional): Date limite

    Returns:
        Task: L'objet Task créé et sauvegardé
    """
    
    # Conversion si strings
    if isinstance(status, str):
        status = TaskStatus(status)
    if isinstance(priority, str):
        priority = TaskPriority(priority)


    session = SessionLocal()
    try:
        new_task = Task(
            theme=theme,
            title=title,
            description=description,
            status=status,
            priority=priority,
            deadline=deadline
        )
        # Ajouter la tâche
        session.add(new_task)
        # Verification
        print("Tentative de création :", theme, title, status, priority, deadline)
        # Enregistrer dans la dbb
        session.commit()
        session.refresh(new_task)
        return new_task

    except Exception as e:
        session.rollback()
        raise RuntimeError(f"Erreur lors de la création de la tâche : {e}") from e

    finally:
        session.close()


# =======================
# Suppression d'une tâche
# =======================    
def delete_task(task_id: int) -> bool:
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()    
        if not task:
            return False
        session.delete(task)
        session.commit()
        return True
    except Exception as e:
        session.rollback()
        raise RuntimeError(f"Erreur lors de la suppression de la tâches : {e}") from e
    finally:
        session.close()
 
 
# =======================
# Modification d'une tâche
# =======================
def update_task(task_id: int, **kwargs) -> Optional[Task]:
    session = SessionLocal()
    try:
        task = session.query(Task).filter(Task.id == task_id).first()
        if not task:
            return None
        for key, value in kwargs.items():
            if hasattr(task, key):
                setattr(task, key, value)
        session.commit()
        session.refresh(task)
        return task
    except Exception as e:
        session.rollback()
        raise RuntimeError(f"Erreur lors de la mise à jour de la tâche : {e}") from e
    finally:
        session.close()        
    
    

# =======================       
# Sérialisation d'une tâche       
# =======================
def serialize_task(task : Task):
    """
    Sérialise un objet Task en dictionnaire pour affichage ou API.

    Args:
        task (Task): Objet Task à sérialiser

    Returns:
        dict: Dictionnaire avec les champs sérialisés
    """
    return {
        "id": task.id,
        "theme": task.theme,
        "title": task.title,
        "status": task.status.value,
        "description": task.description,
        "priority": task.priority.value if task.priority else None,
        "created_at": task.created_at.isoformat() if task.created_at else None,
        "deadline": task.deadline.isoformat() if task.deadline else None
    }
    
    
def get_all_tasks() -> List[Dict[str, Any]]:
    """
    Récupère toutes les tâches triées par deadline et les sérialise.

    Returns:
        List[dict]: Liste de tâches sérialisées
    """
    session = SessionLocal()
    try:
        tasks = session.query(Task).order_by(Task.deadline).all()
        return [serialize_task(task) for task in tasks]
    finally:
        session.close()
        
        