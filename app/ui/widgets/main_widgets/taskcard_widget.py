from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import (
    Qt, pyqtSignal, QPropertyAnimation, QEasingCurve, QRectF, pyqtProperty
)
from PyQt6.QtGui import QColor, QPainter

from app.ui.widgets.main_widgets.subtitle_main_label import SubtitleMainLabel

from app.styles.style_manager import StyleManager


class TaskCard(QWidget):
    clicked = pyqtSignal(dict)

    def __init__(self, task_data):
        super().__init__()
        self.task_data = task_data
        
        # State
        self._overlay_opacity = 0.0
        self._selected = False
        
        
        # Normalisation des clés SQL → Python
        self.title = task_data.get("title", "Sans titre")
        self.status = task_data.get("status", "Inconnu")
        self.priority = task_data.get("priority", "moyenne")
        
        # UI Setup
        self._setup_ui()
        self._setup_animation()
        self._apply_style()
        
        
    #-------------------------
    # INIT UI
    #-------------------------
    def _setup_ui(self):
        self.setObjectName("TaskCard")
        self.setFixedHeight(110)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        
        self.card_layout = QVBoxLayout(self)
        self.card_layout.setContentsMargins(12, 12, 12, 12)
        self.card_layout.setSpacing(3)
        
        self._create_info_labels()
        
        
    def _create_info_labels(self):  
        # Affichage des données
        self.title_label = SubtitleMainLabel(f"Titre : {self.title}")
        self.status_label = SubtitleMainLabel(f"Statut : {self.status}")
        self.priority_label = SubtitleMainLabel(f"Priorité : {self.priority}")
        
        self.card_layout.addWidget(self.title_label)
        self.card_layout.addWidget(self.status_label)
        self.card_layout.addWidget(self.priority_label)

    
    #-------------------------
    # Animation
    #-------------------------
    def _setup_animation(self):
        self.anim = QPropertyAnimation(self, b"overlayOpacity")
        self.anim.setDuration(160)
        self.anim.setEasingCurve(QEasingCurve.Type.OutCubic)
        
    def getOverlayOpacity(self):
        return self._overlay_opacity

    def setOverlayOpacity(self, value):
        self._overlay_opacity = value
        self.update()

    overlayOpacity = pyqtProperty(float, fget=getOverlayOpacity, fset=setOverlayOpacity)


    # ---------------------------------------------------------
    #   STYLE
    # ---------------------------------------------------------
    def _apply_style(self):
        if not self._selected:
            self.setStyleSheet(f"""
                #TaskCard {{
                    background-color: {StyleManager.get('MAIN_BG_COLOR')};
                    border-radius: {StyleManager.get('BORDER_RADIUS')};
                    border: 2px solid {StyleManager.get('BORDER_COLOR')};
                }}
                #TaskCard:hover {{
                    background-color: {StyleManager.get('MAIN_BG_COLOR_HOVER')};
                }}
            """)
        else:
            self.setStyleSheet(f"""
                #TaskCard {{
                    background-color: #2e3a52;
                    border-radius: {StyleManager.get('BORDER_RADIUS')};
                    border: 2px solid {StyleManager.get('BORDER_COLOR')};
                }}
            """)


    # ---------------------------------------------------------
    #   SÉLECTION
    # ---------------------------------------------------------
    def set_selected(self, state: bool):
        self._selected = state
        self._apply_style()

        self.anim.stop()
        self.anim.setStartValue(self._overlay_opacity)
        self.anim.setEndValue(1.0 if state else 0.0)
        self.anim.start()
        
        
    # ---------------------------
    #   CLIC
    # ---------------------------
    def mousePressEvent(self, event):
        if event.button() == Qt.MouseButton.LeftButton:
            self.clicked.emit(self.task_data)
        super().mousePressEvent(event)
    

    # ---------------------------
    #   CUSTOM DRAW : overlay + badge priorité
    # ---------------------------
    def paintEvent(self, event):
        super().paintEvent(event)
        
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Overlay animé
        if self._overlay_opacity > 0:

            glow_color = QColor(94, 160, 255)
            glow_color.setAlphaF(self._overlay_opacity * 0.25)

            painter.setBrush(glow_color)
            painter.setPen(Qt.PenStyle.NoPen)
            painter.drawRoundedRect(QRectF(self.rect()), 12, 12)
        
        # Badge priorité
        self._draw_priority_badge(painter)
        
        
    def _draw_priority_badge(self, painter):
        # Petite pastille en haut à droite."""
        radius = 10
        margin = 8
        color = self._priority_color()

        painter.setBrush(color)
        painter.setPen(Qt.PenStyle.NoPen)

        painter.drawEllipse(
            self.width() - radius * 2 - margin,
            margin,
            radius * 2,
            radius * 2
        )

    def _priority_color(self):
        p = self.priority.lower()
        if p == "haute":
            return QColor(255, 69, 58)   # Rouge
        elif p == "moyenne":
            return QColor(255, 184, 0)  # Jaune
        return QColor(52, 199, 89)     # Vert