from PyQt6.QtWidgets import QLabel

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QColor, QPainter, QBrush



class DotLabel(QLabel):
    """Petit cercle pour la progression"""
    def __init__(self, active=False, size=12, active_color="#E68516", inactive_color="#C4C4C4"):
        super().__init__()
        self.active = active
        self.size = size
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.setFixedSize(QSize(size, size))

    def set_active(self, active: bool):
        self.active = active
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        color = QColor(self.active_color if self.active else self.inactive_color)
        painter.setBrush(QBrush(color))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawEllipse(0, 0, self.size, self.size)