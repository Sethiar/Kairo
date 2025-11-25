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

from app.assets.assets import LOGO, LOGO_LABEL

# Classe pour afficher un logo avec un titre.
class LogoDisplayItem(QWidget):
    """
    Affiche uniquement le logo (SVG/JPG/PNG) avec redimensionnement responsive.
    
    """
    def __init__(self, parent=None):
        super().__init__(parent)

        self.logo_path = LOGO          # Exemple: logo.svg
        self.label_path = LOGO_LABEL   # Exemple: kairo.svg

        self.logo = QLabel()
        self.label = QLabel()

        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # Collé en haut à gauche
        layout.setSpacing(0)

        # --- Logo ---
        if os.path.exists(self.logo_path):
            pixmap = QPixmap(self.logo_path)
            self.logo.setPixmap(
                pixmap.scaledToWidth(250, Qt.TransformationMode.SmoothTransformation)
            )
        else:
            print(f"[BrandHeader] ❌ Logo introuvable : {self.logo_path}")

        self.logo.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        # --- Label (SVG texte Kairo) ---
        if os.path.exists(self.label_path):
            pixmap = QPixmap(self.label_path)
            self.label.setPixmap(
                pixmap.scaledToWidth(160, Qt.TransformationMode.SmoothTransformation)
            )
        else:
            print(f"[BrandHeader] ❌ Label introuvable : {self.label_path}")

        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft | Qt.AlignmentFlag.AlignVCenter)

        # Ajout dans layout
        layout.addWidget(self.logo)
        layout.addWidget(self.label)
        layout.addStretch(1)

        self.setLayout(layout)

    # --- Responsive resize ---
    def resizeEvent(self, event):
        super().resizeEvent(event)

        max_width_logo = min(300, self.width() * 0.30)
        max_width_label = min(220, self.width() * 0.45)

        # LOGO
        if os.path.exists(self.logo_path):
            pix = QPixmap(self.logo_path)
            self.logo.setPixmap(
                pix.scaledToWidth(int(max_width_logo), Qt.TransformationMode.SmoothTransformation)
            )

        # LABEL
        if os.path.exists(self.label_path):
            pix2 = QPixmap(self.label_path)
            self.label.setPixmap(
                pix2.scaledToWidth(int(max_width_label), Qt.TransformationMode.SmoothTransformation)
            )