# app/ui/screen/screen_task/theme_board/task_description_dialog.py

from PyQt6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QScrollArea, QWidget

from PyQt6.QtCore import Qt

from app.ui.widgets.system.label import CustomLabel
from app.ui.widgets.system.hover_button import HoverButton

from app.styles.style_manager import StyleManager

class TaskDescriptionDialog(QDialog):
    
    def __init__(self, task_data, parent=None):
        """
        Dialogue affichant la description d'une tâche.
        Supporte les descriptions longues avec scroll automatique.
        """
        super().__init__(parent)
        
        self.setObjectName("TaskDescriptionDialog")
        
        self.setWindowTitle(task_data.get("title", "Tâche"))
        self.setMinimumWidth(300)
        self.setMaximumWidth(500)
        
        self.setMinimumHeight(300)
        self.setMaximumHeight(600)
        
        desc_layout = QVBoxLayout(self)
        desc_layout.setSpacing(10)
        
        # ScrollArea pour gérer les descriptions très longues
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        desc_layout.addWidget(scroll_area)
        
        scroll_content = QWidget()
        scroll_area.setWidget(scroll_content)
        scroll_layout = QVBoxLayout(scroll_content)
        scroll_layout.setContentsMargins(0, 0, 0, 0)
        scroll_layout.setSpacing(0)
    
        # Description    
        desc_label = CustomLabel(task_data.get("description", "Aucune description"))
        desc_label.setObjectName("DescLabel")
        desc_label.setWordWrap(True)
        desc_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        scroll_layout.addWidget(desc_label)
        
        # Bouton fermer
        close_btn = HoverButton("Fermer")
        close_btn.clicked.connect(self.close)
        
        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        btn_layout.addWidget(close_btn)
        btn_layout.addStretch()
        
        desc_layout.addLayout(btn_layout)
        
        # Appliquer le thème
        self.apply_theme()
        
        
    def apply_theme(self):
        # Style de la fenêtre de decription
        self.setStyleSheet(f"""
            TaskDescriptionDialog {{
                font-size: {StyleManager.get_scaled_font('FONT_SIZE_SETTING')};
                color: {StyleManager.get('TEXT_COLOR_1')};
                background-color: {StyleManager.get('MAIN_BG_COLOR')};
            }}

            #DescLabel {{
                background-color: {StyleManager.get('THEME_BG_COLOR')};
                padding: 8px;              
            }}
        """)
        
        