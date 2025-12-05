from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout
                            )
from PyQt6.QtCore import Qt

from app.core.settings.appearance_logic import AppearanceLogic

from app.ui.widgets.system.hover_button import HoverButton
from app.ui.widgets.system.combo import CustomComboBox
from app.ui.widgets.system.separator import CustomSeparator
from app.ui.widgets.system.label import TitleLabel
from app.ui.widgets.system.label import SubtitleLabel


# Classe de le section affichage des paramètres.
class AppearanceSection(QWidget):
    def __init__(self):
        super().__init__()
        
        self.logic = AppearanceLogic()
        self.setStyleSheet("background: transparent;")

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(30, 10, 30, 20)
        self.main_layout.setSpacing(15)
 
        self._init_title()
        self._init_content()
        self.load_values()
        
        
    # ---------------------------------------------------------
    # TITRE + SÉPARATEUR
    # ---------------------------------------------------------    
    def _init_title(self):
        title_label = TitleLabel("Paramètres d'apparence")
        self.main_layout.addWidget(title_label)
        
        separator = CustomSeparator()
        self.main_layout.addWidget(separator)
        self.main_layout.addSpacing(15)
    
    
    # ---------------------------------------------------------
    # CONTENU PRINCIPAL
    # ---------------------------------------------------------
    def _init_content(self):
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(50, 0, 0, 0)
        content_layout.setSpacing(12)
        
        # Thème
        self.label_theme = SubtitleLabel("Thème :")
        self.combo_theme = CustomComboBox()
        self.combo_theme.addItems(["Light", "Dark"])
        
        theme_layout = QHBoxLayout()
        theme_layout.addWidget(self.label_theme)
        theme_layout.addWidget(self.combo_theme)
        content_layout.addLayout(theme_layout)
        

        # Taille police
        self.label_font = SubtitleLabel("Taille police :")
        self.combo_font = CustomComboBox()
        self.combo_font.addItems(["Petite", "Moyenne", "Grande"])
        
        font_layout = QHBoxLayout()
        font_layout.addWidget(self.label_font)
        font_layout.addWidget(self.combo_font)
        content_layout.addLayout(font_layout)

        self.main_layout.addWidget(content_widget)
        
        self.btn_apply_theme = HoverButton("Appliquer le thème")
        self.btn_apply_theme.clicked.connect(self.on_apply_theme)
        content_layout.addSpacing(20)
        content_layout.addWidget(
            self.btn_apply_theme, 
            alignment=Qt.AlignmentFlag.AlignRight
        )
    
    
    # ---------------------------------------------------------
    # CHARGEMENT DES VALEURS
    # ---------------------------------------------------------
    def load_values(self):
        data = self.logic.load_settings()
        self.combo_theme.setCurrentText(data["theme"])
        self.combo_font.setCurrentText(data["font_size"])

    
    # ---------------------------------------------------------
    # APPLY THEME
    # ---------------------------------------------------------
    def on_apply_theme(self):
        theme = self.combo_theme.currentText()
        font_size = self.combo_font.currentText()
        
        # Sauvegarde
        self.logic.save_settings(theme=theme, font_size=font_size)

        # Application immédiate du thème
        self.logic.theme_manager.set_theme(theme)
        self.logic.theme_manager.set_font_scale(font_size)


        