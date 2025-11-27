"""
Fichier contenant des widgets pour l'affichage des éléments dans l'application Plan-pro.

Auteur: SethiarWorks
Date: 01-12-2025

Description:

Ce module définit plusieurs classes de widgets personnalisés pour l'affichage
des éléments dans l'application en héritant de QWidget.

Il importe également les modules nécessaires de PyQt6 pour la création et la gestion des widgets.
"""

import os

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

from app.assets.assets import LOGO

# Classe pour afficher un logo avec un titre.
class LogoDisplay(QWidget):
    """
    Affiche uniquement le logo (SVG/JPG/PNG) avec redimensionnement responsive.
    
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.logo_label = QLabel()
        self.logo_label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignTop)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.logo_label)
        layout.addStretch(1)  # pousse le logo à gauche
        self.setLayout(layout)

        # Charger le logo
        self._load_logo()

    def _load_logo(self):
        if os.path.exists(LOGO):
            pixmap = QPixmap(LOGO)
            self.logo_label.setPixmap(
                pixmap.scaledToWidth(75, Qt.TransformationMode.SmoothTransformation)
            )
        else:
            print(f"[LogoDisplay] ❌ Logo introuvable : {LOGO}")

        