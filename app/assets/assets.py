import os
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon

# Dossier source de l'application
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Chemin du dossier contenant le logo
LOGO_DIR = os.path.join(BASE_DIR, "assets")

# Logo
LOGO = os.path.join(LOGO_DIR, 'logo.svg')
LOGO_LABEL = os.path.join(LOGO_DIR, "Kairo.svg")

# Chemin vers les icônes
ICONS_DIR = os.path.join(BASE_DIR, "assets", "icons")

LEFT_ARROW_ICON = QIcon(os.path.join(ICONS_DIR, "left_arrow.svg"))
RIGHT_ARROW_ICON = QIcon(os.path.join(ICONS_DIR, "right_arrow.svg"))
ICON_MUSIC = QIcon(os.path.join(ICONS_DIR, "icon_music.svg"))

# Taille standard pour les icônes
ICON_SIZE_LG = QSize(32, 32)
ICON_SIZE_MD = QSize(24, 24)
ICON_SIZE_MN = QSize(20, 20)


# Chemin vers le dossier image
IMAGES_DIR = os.path.join(BASE_DIR, "assets", "images")

# Images du tutoriel
IMAGE_SCREEN0 = os.path.join(IMAGES_DIR, "screen0.jpg")
IMAGE_SCREEN1 = os.path.join(IMAGES_DIR, "screen1.jpg")
IMAGE_SCREEN2 = os.path.join(IMAGES_DIR, "screen2.jpg")
IMAGE_SCREEN3 = os.path.join(IMAGES_DIR, "screen3.jpg")