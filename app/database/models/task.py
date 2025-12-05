# app/database/models/task.py

"""
Module task.py

Contient le modèle SQLAlchemy pour les tâches de la base de données de l'application Kairo.


Auteur : SethiarWorks
Date : 01-01-2026
"""


from enum import Enum
from typing import Optional

from sqlalchemy import Column, Integer, String, DateTime, Enum as SQLEnum, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


Base = declarative_base()


# =======================
# Enum Statut
# =======================
class TaskStatus(str, Enum):
    """Enum pour le statut des tâches."""
    A_FAIRE = "À faire"
    EN_COURS = "En cours"
    TERMINE = "Terminé"
    ANNULEE = "Annulée"
    
    
# =======================
# Enum Priorité
# =======================
class TaskPriority(str, Enum):
    """Enum pour la priorité des tâches."""
    BASSE = "Basse"
    MOYENNE = "Moyenne"
    HAUTE = "Haute"
    URGENTE = "Urgente"
    

# =======================
# Table de données des tâches
# =======================
class Task(Base):
    """
    Modèle représentant une tâche dans le planificateur.

    Attributs :
        id (int): Identifiant unique de la tâche.
        theme (str): Thème de la tâche
        title (str): Titre de la tâche.
        status (str): Statut de la tâche (ex : 'En cours', 'Terminé').
        description (str): Description détaillée.
        priority (str | None): Priorité éventuelle (ex : 'Haute', 'Moyenne').
        created_at (datetime): Date de création, générée automatiquement.
        deadline (datetime | None): Date limite de la tâche.
    """
    __tablename__ = "task"

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    theme: str = Column(String(255), nullable=False)
    title: str = Column(String(255), nullable=False)
    status: TaskStatus = Column(
        SQLEnum(TaskStatus, name="taskstatus", values_callable=lambda x: [e.value for e in x]),
        nullable=False, 
        default=TaskStatus.A_FAIRE  
    )
    description: str = Column(String(1024), nullable=False)
    priority: Optional[TaskPriority] = Column(
        SQLEnum(TaskPriority, name="taskpriority", values_callable=lambda x: [e.value for e in x]),
        nullable=True
    )
    created_at: DateTime = Column(TIMESTAMP, server_default=func.now(), nullable=False)
    deadline: Optional[DateTime] = Column(DateTime, nullable=True)

    def __repr__(self) -> str:
        return (f"<Task(id={self.id}, title={self.title!r}, status={self.status.value}, "
                f"priority={self.priority.value if self.priority else None})>")
    
    
    