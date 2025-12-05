# app/ui/widgets/main_widgets/task_card/task_card.py


from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import Qt, pyqtSignal, QRectF

from app.styles.style_manager import StyleManager

from .task_card_labels import TaskCardLabels
from .priority_badge import get_priority_color
from .task_card_overlay import TaskCardOverlayMixin

from app.ui.screens.screen_tasks.theme_board.task_description_dialog import TaskDescriptionDialog

class TaskCard(QWidget, TaskCardOverlayMixin):
    """
    Carte représentant une tâche.
    """
    
    clicked = pyqtSignal(dict)

    def __init__(self, task_data: dict):
        super().__init__()
        self.setObjectName("TaskCard")
        
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setAutoFillBackground(False)
        
        self.task_data = task_data
        self._overlay_opacity = 0.0
        self._selected = False

        # Layout et labels
        self.labels = TaskCardLabels(task_data)
        self.setLayout(self.labels.layout)

        # Overlay
        self._setup_animation()
        self._apply_style()


    # ---------------------------
    # Style
    # ---------------------------
    def _apply_style(self):
        if not self._selected:
            self.setStyleSheet(f"""
                QWidget#TaskCard {{
                    background-color: {StyleManager.get('CARD_BG_COLOR')};
                    color: {StyleManager.get('TEXT_COLOR_1')};
                    border-radius: {StyleManager.get('BORDER_RADIUS')};
                }}
                QWidget#TaskCard:hover {{
                    background-color: {StyleManager.get('CARD_BG_COLOR_HOVER')};
                }}
            """)
        else:
            self.setStyleSheet(f"""
                QWidget#TaskCard {{
                    background-color: {StyleManager.get('CARD_BG_COLOR_SELECTED')};
                }}                   
            """)
    
    
    # ---------------------------
    # Clic
    # ---------------------------
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            # Afficher la description
            dialog = TaskDescriptionDialog(self.task_data, self)
            dialog.exec()
            
            # Émettre signal
            self.clicked.emit(self.task_data)
            
        super().mousePressEvent(event)
        
        
    # ---------------------------
    # Paint + Overlay
    # ---------------------------   
    def paintEvent(self, event):
        # Overlay et badge
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Overlay animé
        if self._overlay_opacity > 0:
            glow_color = QColor(94, 160, 255)
            glow_color.setAlphaF(self._overlay_opacity * 0.8)
            painter.setBrush(glow_color)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRoundedRect(QRectF(self.rect()), 12, 12)

        # Badge priorité
        radius = 10
        margin = 8
        color = get_priority_color(self.task_data.get("priority", "moyenne"))
        painter.setBrush(color)
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(
            self.width() - radius * 2 - margin,
            margin,
            radius * 2,
            radius * 2
        )
        
        