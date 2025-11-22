
import os

from typing import List, Optional

from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput



class MusicLogic:
    """
    Logique métier : stockage des chemins, ajout/suppression, preview audio.
    Ne contient aucun widget Qt (sauf le player qui est un objet non-graphique).
    """
    def __init__(self, parent=None):
        # player + audio output (séparés dans Qt6)
        self.player = QMediaPlayer(parent)
        self.audio_output = QAudioOutput(parent)
        self.player.setAudioOutput(self.audio_output)
        
        # Liste des fichiers (chemins complets)
        self.music_files = []
        
    #-------------------
    # Gestion de la liste
    #-------------------  
    def add_files(self, files: list[str]):
        """Ajoute une liste de chemins (pré-filtrés par l'UI)."""
        if not files:
            return
        for f in files:
            if f not in self.music_files:
                self.music_files.append(f)


    def add_folder(self, folder: str):
        """Ajoute tous les fichiers audio du dossier (non récursif)."""
        if not folder:
            return
        for file in os.listdir(folder):
            if file.lower().endswith((".mp3", ".wav", ".flac")):
                full_path = os.path.join(folder, file)
                if full_path not in self.music_files:
                    self.music_files.append(full_path)
    
    
    def remove_file(self, path: str):
        """Supprime un fichier de la bibliothèque si présent."""            
        if path in self.music_files:
            self.music_files.remove(path)
            
            
    def clear(self):
        """Vide la bobliothèque."""
        self.music_files.clear()
        
        
    #-------------------
    # Preview / lecture
    #-------------------
    def preview(self, file_path: str):
        """Démarre la lecture d'un fichier."""
        if not file_path or not os.path.exists(file_path):
            return
        
        # Stop current
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.stop()
        
        qurl = QUrl.fromLocalFile(file_path)
        self.player.setSource(qurl)
        
        # Volume / Options peuvent étre ecposées si besoin
        self.audio_output.setVolume(0.6)
        self.player.play()
        
    
    def stop_preview(self):
        if self.player.playbackState() != QMediaPlayer.PlaybackState.StoppedState:
            self.player.stop()
        
    def toggle_play_pause(self):
        state = self.player.playbackState()
        if state == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            self.player.play()    