# Kairo/app/assets/assets.py

"""
Module assets.py

Ce module centralise lea gestion des chemins et des ressources graphiques
de l'applicaiton Kairo. Il définit les chemins vers les logos, les icônes,
images, ainsi que les tailles standards pour les icônes.

Auteur : SethiarWorks
Date : 01-01-2026
"""


import os
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon


# =======================
# Définition des dossiers
# =======================

# Dossier racine de l'application
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
"""
BASE_DIR: str
Chemin absolu vers le dossier racine de l'application.
"""


# Dossier contenant les ressources graphiques
LOGO_DIR = os.path.join(BASE_DIR, "assets")
# Chemin vers le dossier image
IMAGES_DIR = os.path.join(BASE_DIR, "assets", "images")
# Chemin vers les icônes
ICONS_DIR = os.path.join(BASE_DIR, "assets", "icons")
"""
LOGO_DIR, IMAGES_DIR, ICONS_DIR : str
Chemins vers les dossiers de ressources de l'application.
"""


# =======================
# Logos
# =======================
LOGO = os.path.join(LOGO_DIR, 'logo.svg')
LOGO_LABEL = os.path.join(LOGO_DIR, "Kairo.svg")
"""
LOGO, LOGO_LABEL : str
Chemins vers les fichiers de logo principaux.
"""


# =======================
# Icônes
# =======================
LEFT_ARROW_ICON = QIcon(os.path.join(ICONS_DIR, "left_arrow.svg"))
RIGHT_ARROW_ICON = QIcon(os.path.join(ICONS_DIR, "right_arrow.svg"))
ICON_MUSIC = QIcon(os.path.join(ICONS_DIR, "icon_music.svg"))
"""
LEFT_ARROW_ICON, RIGHT_ARROW_ICON, ICON_MUSIC : QIcon
Objets QIcon pour les icônes de navigation et musique.
"""

# Taille standard pour les icônes
ICON_SIZE_LG = QSize(32, 32)
ICON_SIZE_MD = QSize(24, 24)
ICON_SIZE_MN = QSize(20, 20)
"""
ICON_SIZE_LG, ICON_SIZE_MD, ICON_SIZE_MN : QSize
Taille standard des icônes pour une utilisation cohérente dans l'UI.
"""

# =======================
# Images du tutoriel
# =======================
IMAGE_SCREEN0 = os.path.join(IMAGES_DIR, "screen0.jpg")
IMAGE_SCREEN1 = os.path.join(IMAGES_DIR, "screen1.jpg")
IMAGE_SCREEN2 = os.path.join(IMAGES_DIR, "screen2.jpg")
IMAGE_SCREEN3 = os.path.join(IMAGES_DIR, "screen3.jpg")
"""
IMAGE_SCREEN0-3 : str
Chemins vers les images utilisées dans le tutoriel.
"""