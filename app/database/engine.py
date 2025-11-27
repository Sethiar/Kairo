# app/database/engine.py

"""
Module engine.py

Configuration de la base de données pour l'application Kairo.

- Chargement des variables d'environnement via dotenv
- Création de l'engine SQLAlchemy
- Création de la session factory (SessionLocal)


Auteur : SethiarWorks
Date : 01-01-2026
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from dotenv import load_dotenv

load_dotenv()

# =======================
# Variables d'environnement
# =======================
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")

# URL de connexion
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# =======================
# Engine SQLAlchemy
# =======================
engine = create_engine(
    DATABASE_URL,
    echo=True,
    future=True
)

# =======================
# Session factory
# =======================
SessionLocal = sessionmaker(
    bind=engine,
    autocommit=False,
    autoflush=False,
    future=True)

"""
SessionLocal : factory pour créer des sessions SQLAlchemy.
Exemple :
    with SessionLocal() as session:
        session.query(Task).all()
"""