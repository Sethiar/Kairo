from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox,
                            QFrame
                            )


from app.core.settings.appearence_logic import AppearenceLogic
from app.styles.style_manager import StyleManager
from app.ui.screens.settings.settings_widgets.hover_button import HoverButton

from app.ui.screens.settings.settings_widgets.custom_widgets import CustomComboBox
from app.ui.screens.settings.settings_widgets.title_lable import TitleLabel



class AppearenceSection(QWidget):
    def __init__(self):
        super().__init__()
        self.logic = AppearenceLogic()

        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(30, 10, 30, 20)
        self.main_layout.setSpacing(15)
 
        self._init_title()
        self._init_content()
        self.load_values()
        
        
    def _init_title(self):
        self.title_label = TitleLabel("Paramètres d'apparence")
        self.main_layout.addWidget(self.title_label)
        
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setStyleSheet(f"background-color: {StyleManager.get('LINE_COLOR')};")
        separator.setFixedHeight(2)
        self.main_layout.addWidget(separator)
        self.main_layout.addSpacing(15)

    def _init_content(self):
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)

        # Thème
        self.label_theme = QLabel("Thème :")
        self.combo_theme = CustomComboBox()
        self.combo_theme.addItems(["Light", "Dark"])
        theme_layout = QHBoxLayout()
        theme_layout.addWidget(self.label_theme)
        theme_layout.addWidget(self.combo_theme)
        content_layout.addLayout(theme_layout)

        self.btn_apply_theme = HoverButton("Appliquer le thème")
        self.btn_apply_theme.clicked.connect(self.on_apply_theme)
        content_layout.addWidget(self.btn_apply_theme)

        # Taille police
        self.label_font = QLabel("Taille police :")
        self.combo_font = CustomComboBox()
        self.combo_font.addItems(["Grande", "Normal", "Petite"])
        font_layout = QHBoxLayout()
        font_layout.addWidget(self.label_font)
        font_layout.addWidget(self.combo_font)
        content_layout.addLayout(font_layout)

        self.main_layout.addWidget(content_widget)
        self.main_layout.addStretch()

    def load_values(self):
        data = self.logic.load_settings()
        self.combo_theme.setCurrentText(data["theme"])
        self.combo_font.setCurrentText(data["font_size"])

    def on_apply_theme(self):
        theme = self.combo_theme.currentText()
        font_size = self.combo_font.currentText()

        self.logic.save_settings(theme=theme, font_size=font_size)

        # Application immédiate du thème
        self.logic.theme_manager.set_theme(theme)

    def apply_theme_to_widgets(self):
        self.setStyleSheet(f"background-color: {StyleManager.get('BACKGROUND_COLOR')};")
        self.title_label.setStyleSheet(f"font-weight:{StyleManager.get('FONT_WEIGHT_BOLD')}; color:{StyleManager.get('TEXT_COLOR_1')}")
        self.label_theme.setStyleSheet(f"color:{StyleManager.get('TEXT_COLOR_1')}")
        self.label_font.setStyleSheet(f"color:{StyleManager.get('TEXT_COLOR_1')}")
        self.btn_apply_theme.setStyleSheet(f"background-color:{StyleManager.get('BTN_SETTING_BG_COLOR')}; color:{StyleManager.get('BUTTON_FG')}")
        