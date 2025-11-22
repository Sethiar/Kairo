from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QPushButton, QSizePolicy
from PyQt6.QtCore import Qt, pyqtSignal

from app.assets.assets import LEFT_ARROW_ICON, RIGHT_ARROW_ICON

from .screens import Screen0, Screen1, Screen2, Screen3
from .dot_label import DotLabel  

class IntroScreen(QWidget):
    
    # signal pour le menu ou parent
    screenChanged = pyqtSignal(str)  

    def __init__(self):
        super().__init__()
        self.current_index = 0
        self.screens = {
            "screen0": Screen0(self),
            "screen1": Screen1(self),
            "screen2": Screen2(self),
            "screen3": Screen3(self)
        }

        self.stack = QStackedWidget()
        for screen in self.screens.values():
            self.stack.addWidget(screen)

        self.dots = [DotLabel(active=(i==0)) for i in range(len(self.screens))]

        self._build_layout()
        self.show_screen("screen0")

    def _build_layout(self):
        layout = QVBoxLayout()
        layout.setContentsMargins(20,20,20,20)
        layout.setSpacing(15)
        self.setLayout(layout)

        # stacked widget
        self.stack.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout.addWidget(self.stack)

        # navigation
        nav_layout = QHBoxLayout()
        self.prev_btn = QPushButton()
        self.prev_btn.setIcon(LEFT_ARROW_ICON)
        self.prev_btn.setFixedSize(50,50)
        self.prev_btn.clicked.connect(self.prev_screen)

        self.next_btn = QPushButton()
        self.next_btn.setIcon(RIGHT_ARROW_ICON)
        self.next_btn.setFixedSize(50,50)
        self.next_btn.clicked.connect(self.next_screen)

        nav_layout.addWidget(self.prev_btn)
        nav_layout.addStretch()
        nav_layout.addWidget(self.next_btn)
        layout.addLayout(nav_layout)

        # dots
        dot_layout = QHBoxLayout()
        dot_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        for dot in self.dots:
            dot_layout.addWidget(dot)
        layout.addLayout(dot_layout)

    def show_screen(self, screen_id: str):
        if screen_id not in self.screens:
            print(f"[IntroScreen] screen '{screen_id}' inconnu")
            return
        self.current_index = list(self.screens.keys()).index(screen_id)
        self.stack.setCurrentWidget(self.screens[screen_id])
        for i, dot in enumerate(self.dots):
            dot.set_active(i == self.current_index)
        self.prev_btn.setEnabled(self.current_index > 0)
        self.next_btn.setEnabled(self.current_index < len(self.screens)-1)
        self.screenChanged.emit(screen_id)

    def next_screen(self):
        keys = list(self.screens.keys())
        if self.current_index < len(keys)-1:
            self.show_screen(keys[self.current_index+1])

    def prev_screen(self):
        keys = list(self.screens.keys())
        if self.current_index > 0:
            self.show_screen(keys[self.current_index-1])