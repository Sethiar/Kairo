from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QFileDialog
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QCursor

from app.core.settings.user_logic import UserLogic
from app.styles.style_manager import StyleManager

from app.ui.widgets.system.hover_button import HoverButton
from app.ui.widgets.system.label import SubtitleLabel
from app.ui.widgets.system.line_edit import CustomLineEdit
from app.ui.widgets.system.separator import CustomSeparator
from app.ui.widgets.system.label import TitleLabel



class UserSection(QWidget):
    AVATAR_SIZE = 120

    def __init__(self):
        super().__init__()
        self.logic = UserLogic()
        self.setStyleSheet("background: transparent;")

        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(30, 10, 30, 20)
        self.main_layout.setSpacing(15)
        self.setLayout(self.main_layout)

        self._init_title()
        self._init_content()
        self.load_values()

    # --------------------
    # TITRE + SEPARATEUR
    # --------------------
    def _init_title(self):
        title_label = TitleLabel('Paramètres utilisateur')
        self.main_layout.addWidget(title_label, alignment=Qt.AlignmentFlag.AlignTop)

        separator = CustomSeparator()
        self.main_layout.addWidget(separator)
        self.main_layout.addSpacing(15)

    # --------------------
    # CONTENU : AVATAR + FORM
    # --------------------
    def _init_content(self):
        content_widget = QWidget()
        content_layout = QHBoxLayout()
        content_layout.setContentsMargins(50, 0, 0, 0)
        content_layout.setSpacing(60)
        content_widget.setLayout(content_layout)

        # --- FORM ---
        form_layout = QVBoxLayout()
        form_layout.setSpacing(18)

        self.input_name = self._add_labeled_input("Nom :", form_layout)
        self.input_email = self._add_labeled_input("Email :", form_layout)
        self.enable_notifications = QCheckBox("Activer les notifications")
        form_layout.addWidget(self.enable_notifications)
        
        # --- AVATAR ---
        avatar_layout = QVBoxLayout()
        avatar_layout.setSpacing(12)
        avatar_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        self.avatar_label = QLabel()
        self.avatar_label.setFixedSize(self.AVATAR_SIZE, self.AVATAR_SIZE)
        self.avatar_label.setStyleSheet(f"border-radius: {StyleManager.get('BORDER_RADIUS_IMAGE')};")
        self.avatar_label.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.avatar_label.mousePressEvent = lambda e: self.on_change_avatar()

        self.btn_avatar = HoverButton("Changer l'avatar", width=160, height=40)
        self.btn_avatar.clicked.connect(self.on_change_avatar)

        avatar_layout.addWidget(self.avatar_label, alignment=Qt.AlignmentFlag.AlignLeft)
        avatar_layout.addWidget(self.btn_avatar, alignment=Qt.AlignmentFlag.AlignLeft)
        
        content_layout.addLayout(form_layout)
        content_layout.setSpacing(200)
        content_layout.addLayout(avatar_layout)

       
        self.main_layout.addWidget(content_widget)

    # --------------------
    # INPUT FACTORY
    # --------------------
    def _add_labeled_input(self, label_text: str, parent_layout: QVBoxLayout):
        layout = QHBoxLayout()
        layout.setSpacing(10)

        label = SubtitleLabel(label_text)
        label.setFixedWidth(120)
        
        input_field = CustomLineEdit(width=250)
    
        layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(label)
        layout.addWidget(input_field)
        parent_layout.addLayout(layout)

        return input_field


    # --------------------
    # LOGIC
    # --------------------
    def load_values(self):
        data = self.logic.load_user_settings()
        self.input_name.setText(data["name"])
        self.input_email.setText(data["email"])
        self.enable_notifications.setChecked(data["notifications_enabled"])
        self.avatar_label.setPixmap(self.logic.get_avatar_pixmap(size=self.AVATAR_SIZE))

    def on_save(self):
        if not self.input_name.text().strip():
            self._show_error("Le nom ne peut pas être vide.")
            return
        if "@" not in self.input_email.text():
            self._show_error("Adresse email invalide.")
            return

        self.logic.save_user_settings(
            name=self.input_name.text(),
            email=self.input_email.text(),
            notifications_enabled=self.enable_notifications.isChecked()
        )

    def on_change_avatar(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Sélectionner un avatar", "", "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if not file_path:
            return

        self.logic.save_user_settings(
            name=self.input_name.text(),
            email=self.input_email.text(),
            notifications_enabled=self.enable_notifications.isChecked(),
            avatar_path=file_path
        )
        self.avatar_label.setPixmap(self.logic.get_avatar_pixmap(size=self.AVATAR_SIZE, path=file_path))

    # --------------------
    # UTILS
    # --------------------
    def _show_error(self, msg: str):
        from PyQt6.QtWidgets import QMessageBox
        QMessageBox.warning(self, "Erreur", msg)