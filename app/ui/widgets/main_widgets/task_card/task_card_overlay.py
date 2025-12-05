# app/ui/widgets/main_widgets/task_card/task_card_overlay.py


from PyQt6.QtCore import QPropertyAnimation, QEasingCurve, pyqtProperty

class TaskCardOverlayMixin:
    """
    Mixin pour gérer l'overlay animé et la sélection.
    """
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
    
    
    def set_selected(self, state: bool):
        self._selected = state
        self._apply_style()
        self.anim.stop()
        self.anim.setStartValue(self._overlay_opacity)
        self.anim.setEndValue(1.0 if state else 0.0)
        self.anim.start()