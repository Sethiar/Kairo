from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QFrame, QSizePolicy
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from app.styles.style_manager import StyleManager

from app.assets.assets import IMAGE_SCREEN0, IMAGE_SCREEN1, IMAGE_SCREEN2, IMAGE_SCREEN3

class ScreenBase(QWidget):
    """Screen générique pour tutoriel, bullets à gauche, image à droite."""
    
    def __init__(self, title: str, subtitle: str, features: list, image_path: str = None, parent=None):
        super().__init__(parent)
        
        # Layout principal vertical
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(40, 80, 40, 40)
        self.main_layout.setSpacing(30)
        self.setLayout(self.main_layout)
        
        # Titre
        self.title_label = QLabel(title)
        self._style_label(self.title_label, StyleManager.get('FONT_SIZE_TITLE'), True)
        self.main_layout.addWidget(self.title_label, alignment=Qt.AlignmentFlag.AlignLeft)
        
        # Sous-titre
        self.subtitle_label = QLabel(subtitle)
        self.subtitle_label.setWordWrap(True)
        self._style_label(self.subtitle_label, StyleManager.get('FONT_SIZE_INTRO_SENTENCE'), True)
        self.main_layout.addWidget(self.subtitle_label, alignment=Qt.AlignmentFlag.AlignLeft)
        
        # Ligne séparatrice
        self.separator = QFrame()
        self.separator.setFixedHeight(int(StyleManager.get('LINE_HEIGHT').replace("px", "")))
        self.separator.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        self.separator.setStyleSheet(f"background-color: {StyleManager.get('LINE_COLOR')}; border: none;")
        self.main_layout.addSpacing(20)
        self.main_layout.addWidget(self.separator)
        self.main_layout.addSpacing(20)
        
        # Layout horizontal pour contenu
        self.content_layout = QHBoxLayout()
        self.content_layout.setSpacing(40)
        self.main_layout.addLayout(self.content_layout)
        
        # Colonne gauche pour bullets
        self.bullets_layout = QVBoxLayout()
        self.bullets_layout.setSpacing(int(StyleManager.get('DEFAULT_SPACING').replace("px", "")))
        self.content_layout.addLayout(self.bullets_layout, 2)
        
        # Ajouter bullets
        self._add_bullets(features)
        
        # Colonne droite pour image
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        if image_path:
            pixmap = QPixmap(image_path)
            # Redimensionner à 50x50 tout en gardant les proportions
            pixmap = pixmap.scaled(
                100, 100,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.image_label.setPixmap(pixmap)

        self.content_layout.addWidget(self.image_label, 1)
    
    
    def _style_label(self, label: QLabel, font_size: str, bold: bool = False):
        weight = StyleManager.get('FONT_WEIGHT_BOLD') if bold else StyleManager.get('FONT_WEIGHT_NORMAL')
        label.setStyleSheet(f"""
            font-size: {font_size};
            font-weight: {weight};
            color: {StyleManager.get('TEXT_COLOR_2')};
        """)
    
    def _add_bullets(self, features: list):
        for f in features:
            lbl = QLabel(f"• {f}")
            lbl.setWordWrap(True)
            self._style_label(lbl, StyleManager.get('FONT_SIZE_BULLET'), False)
            lbl.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
            self.bullets_layout.addWidget(lbl)


# Exemple de screens avec cette factory
features0 = [
    "Naviguez grâce à une interface claire et moderne",
    "Créez et organisez vos tâches en 3 clics",
    "Personnalisez et travailler à votre rythme",
    "Gardez sous contrôle votre planning et productivité"
]
Screen0 = lambda parent=None: ScreenBase("Kairo", "Optimisez votre temps de travail de manière simple et intelligente", features0, IMAGE_SCREEN0, parent)

features1 = [
    "Planifiez vos projets étape par étape",
    "Organisez vos journées et vos priorités",
    "Suivie de production et respect des deadlines",
    "Restez concentré et atteignez vos objectifs"
]
Screen1 = lambda parent=None: ScreenBase("Kairo", "Optimisez vos projets", features1, IMAGE_SCREEN1, parent)

features2 = [
    "Choisissez vos couleurs et votre style visuel",
    "Visualisez planning et tâches d'un coup d’œil",
    "Ajustez les notifications et l’ambiance sonore",
    "Tous vos outils de gestion réunis ici"
]
Screen2 = lambda parent=None: ScreenBase("Kairo", "Personnalisez votre interface", features2, IMAGE_SCREEN2, parent)

features3 = [
    "Suivez vos progrès et vos accomplissements",
    "Adaptez votre rythme et restez productif",
    "Recevez des rappels et des conseils",
    "Devenez maître de votre organisation avec Kairo"
]
Screen3 = lambda parent=None: ScreenBase("Kairo", "Bilan et productivité", features3, IMAGE_SCREEN3, parent)