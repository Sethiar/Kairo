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


def create_task(
    title: str, description: str,
    status: TaskStatus = TaskStatus.PENDING,
    priority: Optional[TaskPriority] = None,
    deadline: Optional[datetime] = None
) -> Task:
    
    """
    Crée une nouvelle tâche et la sauvegarde en base de données.

    Args:
        title (str): Titre de la tâche
        description (str): Description détaillée
        status (TaskStatus, optional): Statut de la tâche
        priority (TaskPriority, optional): Priorité
        deadline (datetime, optional): Date limite

    Returns:
        Task: L'objet Task créé et sauvegardé
    """
    session = SessionLocal()
    try:
        new_task = Task(
            title=title,
            description=description,
            status=status,
            priority=priority,
            deadline=deadline
        )
        # Ajouter la tâche
        session.add(new_task)
        # Enregistrer dans la dbb
        session.commit()
        session.refresh(new_task)
        return new_task

    except Exception as e:
        session.rollback()
        raise RuntimeError(f"Erreur lors de la création de la tâche : {e}") from e

    finally:
        session.close()
            

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
        "title": task.title,
        "status": task.status.value,       # utilisation de l'enum
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
        
        