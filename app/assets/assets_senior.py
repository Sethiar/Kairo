# Kairo/app/assets/assets.py

"""
Module assets.py

Centralise la gestion des ressources graphiques de l'application Kairo.
Permet d'accéder aux logos, icônes, images et tailles standard d'icônes.
Vérifie l'existence des fichiers pour éviter les erreurs silencieuses.

Auteur : Arnaud
"""

import os
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
import warnings


class Assets:
    """
    Classe Assets

    Fournit un accès centralisé aux logos, icônes et images de l'application.
    Vérifie l'existence des fichiers et fournit des tailles standard pour les icônes.
    """

    # =======================
    # Dossiers
    # =======================
    # Enregistrement du chemin absolu du dossier source
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Enregistrement du chemin absolu du dossier des assets
    ASSETS_DIR = os.path.join(BASE_DIR, "assets")
    # Enregistrement du chemin absolu du dossier des icônes
    ICONS_DIR = os.path.join(ASSETS_DIR, "icons")
    # Enregistrement du chemin absolu du dossier des images
    IMAGES_DIR = os.path.join(ASSETS_DIR, "images")

    # =======================
    # Logos
    # =======================
    # Dictionnaire reliant les différentes versions du logo en fonction de leur emplacement
    logos = {
        "main": os.path.join(ASSETS_DIR, "logo.svg"),
        "label": os.path.join(ASSETS_DIR, "Kairo.svg"),
    }

    # =======================
    # Icônes
    # =======================
    # Dictionnaire reliant les différents icônes
    icons = {
        "left_arrow": QIcon(os.path.join(ICONS_DIR, "left_arrow.svg")),
        "right_arrow": QIcon(os.path.join(ICONS_DIR, "right_arrow.svg")),
        "music": QIcon(os.path.join(ICONS_DIR, "icon_music.svg")),
    }

    # Tailles standard pour les icônes
    icon_sizes = {
        "lg": QSize(32, 32),
        "md": QSize(24, 24),
        "mn": QSize(20, 20),
    }

    # =======================
    # Images du tutoriel
    # =======================
    tutorial_images = [
        os.path.join(IMAGES_DIR, f"screen{i}.jpg") for i in range(4)
    ]

    # =======================
    # Méthodes
    # =======================
    @classmethod
    def verify_files(cls):
        """
        Vérifie que tous les fichiers listés existent.
        Affiche un warning si un fichier est manquant.
        """
        all_files = list(cls.logos.values()) + cls.tutorial_images
        # Itération sur les clés et des icônes
        for key, icon in cls.icons.items():
            # QIcon n'a pas de chemin direct, on ne peut pas vérifier l'existence ici
            continue

        for file_path in all_files:
            if not os.path.exists(file_path):
                warnings.warn(f"Fichier manquant : {file_path}")


    @classmethod
    def get_icon(cls, name: str) -> QIcon:
        """
        Retourne un QIcon correspondant au nom donné.

        Args:
            name (str): Nom de l'icône ('left_arrow', 'right_arrow', 'music', etc.)

        Returns:
            QIcon: L'icône correspondante.
        """
        return cls.icons.get(name, QIcon())


    @classmethod
    def get_logo(cls, name: str) -> str:
        """
        Retourne le chemin vers un logo.

        Args:
            name (str): Nom du logo ('main', 'label').

        Returns:
            str: Chemin du logo.
        """
        return cls.logos.get(name, "")


    @classmethod
    def get_tutorial_images(cls) -> list[str]:
        """
        Retourne la liste des images du tutoriel.

        Returns:
            list[str]: Liste des chemins vers les images.
        """
        return cls.tutorial_images


    @classmethod
    def get_icon_size(cls, size: str) -> QSize:
        """
        Retourne la taille standard d'une icône.

        Args:
            size (str): Taille souhaitée ('lg', 'md', 'mn').

        Returns:
            QSize: Taille correspondante.
        """
        return cls.icon_sizes.get(size, QSize(24, 24))


# =======================
# Vérification à l'import
# =======================
Assets.verify_files()