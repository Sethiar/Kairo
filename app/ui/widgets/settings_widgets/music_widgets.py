import os 

from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QFileDialog, QListWidget, 
    QListWidgetItem, QLabel, QSpacerItem, QSizePolicy
)
from PyQt6.QtCore import Qt, QSize

from app.core.settings.music_logic import MusicLogic
from app.ui.widgets.system.hover_button import HoverButton

from app.assets.assets import ICON_MUSIC


class MusicWidget(QWidget):
    """
    Widget UI utiisant MusicLogic.
    - Boutons add files / add folder / Remove / Preview
    - Liste avec icônes + tooltip
    - Play / Pause / Stop
    """
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.logic = MusicLogic(parent=self)
        self._built_ui()
        self._connect_signals()
        
    def _built_ui(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(10)
        
        # Boutons
        row = QHBoxLayout()
        self.btn_add_files = HoverButton("Ajouter de fichiers")
        self.btn_add_folder = HoverButton("Ajouter un dossier")
        self.btn_remove = HoverButton("Supprimer la sélection")
        
        row.addWidget(self.btn_add_files)
        row.addWidget(self.btn_add_folder)
        row.addWidget(self.btn_remove)
        row.addSpacerItem(
            QSpacerItem(
                10, 10, 
                QSizePolicy.Policy.Expanding, 
                QSizePolicy.Policy.Minimum
                )
            )
        
        self.main_layout.addLayout(row)
        
        # Contrôle de la lecture
        ctrl_row = QHBoxLayout()
        self.btn_play_pause = HoverButton("Lecture/Pause")
        self.btn_stop = HoverButton("Stop")
        ctrl_row.addWidget(self.btn_play_pause)
        ctrl_row.addWidget(self.btn_stop)
        ctrl_row.addSpacerItem(
            QSpacerItem(
                10, 10, 
                QSizePolicy.Policy.Expanding, 
                QSizePolicy.Policy.Minimum
                )
            )
        self.main_layout.addLayout(ctrl_row)
        
        # QListWidget affichage des icônes (vertical)
        self.list_widget = QListWidget()
        self.list_widget.setViewMode(QListWidget.ViewMode.ListMode)
        self.list_widget.setIconSize(QSize(40, 40))
        self.list_widget.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)
        self.main_layout.addWidget(self.list_widget)
        
        # Label d'intro (Durée / Chemin)
        self.info_label = QLabel("")
        self.main_layout.addWidget(self.info_label)
        
        
    def _apply_styles(self):
        # styles simples réutilisant StyleManager
        self.list_widget.setStyleSheet(f"""
            QListWidget {{
                background: transparent;
            }}
            QListWidget::item {{
                padding: 8px;
            }}
        """)
            
    
    def _connect_signals(self):    
        self.btn_add_files.clicked.connect(self._on_add_files)
        self.btn_add_folder.clicked.connect(self._on_add_folder)
        self.btn_remove.clicked.connect(self._on_remove_selected)
        self.btn_play_pause.clicked.connect(self._on_play_pause)
        self.btn_stop.clicked.connect(self._on_stop)
        self.list_widget.itemDoubleClicked.connect(self._on_item_double_clicked)
        
    
    #-------------------------
    # UI Handlers    
    #-------------------------
    def _on_add_files(self):
        files, _ = QFileDialog.getOpenFileName(
            self, "Sélectionner des fichiers musicaux","", "Fichiers audio (*.mp3 *.wav *.flac *.ogg *.m4a)"
        )
        # files est une listes
        self.logic.add_files(files)    
        self._update_list_widget()
        
    def _on_add_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Sélectionner un dossier musical")
        self.logic.add_folder(folder)
        self._update_list_widget()
        
    def _on_remove_selected(self):
        items = self.list_widget.selectedItems()
        if not items:
            return
        for it in items:
            path = it.data(Qt.ItemDataRole.UserRole)
            self.logic.remove_file(path)
        self._update_list_widget()
        
    def _on_play_pause(self):
        # Toggle play/pause via logic
        self.logic.toggle_play_pause()
        # update info label
        self._update_info_label()
        
    def _on_stop(self):
        self.logic.stop_preview()
        self._update_info_label()
        
    def _on_item_double_clicked(self, item:QListWidgetItem):
        " Double-click => play"
        path = item.data(Qt.ItemDataRole.UserRole)
        self.logic.preview(path)
        self._update_info_label()
        
        
    #-------------------------
    # Helpers UI <--> Logic
    #-------------------------
    def _update_list_widget(self):
        """Remplir la QListWidget avec les données musicales"""
        self.list_widget.clear()
        default_icon = self._get_default_icon()
        for path in self. logic.music_files:
            name = os.path.basename(path)
            it = QListWidgetItem()
            it.setText(name)
            it.setToolTip(path)
            it.setData(Qt.ItemDataRole.UserRole, path)
            it.setIcon(default_icon)
            self.list_widget.addItem(it)
            
    def _get_default_icon(self):
        # Chargment d'un icêone d'assets.
        icon = ICON_MUSIC
        return icon
    
    def _update_info_label(self):
        state = self.logic.player.playbackState()
        if state == self.logic.player.PlaybackState.PlayingState:
            status = "Lecture"
        elif state == self.logic.player.PlaybackState.PausedState:
            status = "Pause"
        else:
            status = "Arrêt"
        
        current = ""
        cur_item = self.list_widget.currentItem()
        if cur_item:
            current = cur_item.data(Qt.ItemDataRole.UserRole) 
        self.info_label.setText(f"{status} - {current}")         