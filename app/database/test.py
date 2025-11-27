# app/database/example_task.py
from sqlalchemy import create_engine, Column, Integer, String, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from dotenv import load_dotenv
import os

# Charger les variables d'environnement
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Connexion à la base
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

# Définition du modèle Task
Base = declarative_base()

class Task(Base):
    __tablename__ = "Tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    status = Column(String(100), nullable=False)
    priority = Column(String(50))
    created_at = Column(TIMESTAMP, server_default=func.now())

# Créer la table si elle n'existe pas
Base.metadata.create_all(engine)

# Créer une tâche exemple
example_task = Task(
    title="Tâche exemple",
    status="À faire",
    priority="Haute"
)

# Ajouter à la base
session.add(example_task)
session.commit()

print(f"Tâche '{example_task.title}' ajoutée avec l'ID {example_task.id}")