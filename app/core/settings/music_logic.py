# app/core/music_logic.py

"""
Module music_logic.py

Logique métier pour la gestion de la bibliothèque musicale.
Gère la liste de fichiers audio, l'ajout/suppression de fichiers ou dossiers,
et la lecture/preview audio.

Ne contient aucun widget graphique Qt, sauf les objets non-visuels QMediaPlayer et QAudioOutput.

Auteur : SethiarWorks
Date : 01-01-2026
"""

import os

from typing import List

from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QMediaPlayer, QAudioOutput



class MusicLogic:
    """
    Classe MusicLogic

    Encapsule la logique de gestion de la bibliothèque musicale.

    Attributs :
        player (QMediaPlayer) : Player audio non-graphique.
        audio_output (QAudioOutput) : Gestion du volume et sortie audio.
        music_files (list[str]) : Liste des chemins des fichiers audio.
    """
    # Déclaration des fichiers de musique supportés
    SUPPORTED_EXTENSIONS = (".mp3", ".wav", ".flac")
    
    # Initialilsation de la classe
    def __init__(self, parent=None):
        """
        Initialise MusicLogic avec un player et audio output.

        Args:
            parent (Optional[QObject]): Parent Qt pour le player/audio.
        """
        # Instanciation du lecteur du média
        self.player: QMediaPlayer = QMediaPlayer(parent)
        # Instanciation de la sortie audio
        self.audio_output: QAudioOutput = QAudioOutput(parent)
        # Validation de la sortie audio pour le lecteur audio
        self.player.setAudioOutput(self.audio_output)
        
        # Liste des fichiers (chemins complets)
        self.music_files: List[str] = []
        
        
    # =======================
    # Gestion de la bibliothèque
    # =======================
    
    # Méthode ajoutant un fichier
    def add_files(self, files: list[str]):
        """
        Ajoute une liste de fichiers à la bibliothèque.

        Les fichiers sont pré-filtrés par l'UI.

        Args:
            files (list[str]): Liste de chemins de fichiers audio.
        """
        # Vérification de la présence des fichiers
        if not files:
            return
        # Itération des fichiers du dossier
        for f in files:
            # Condition d'ajout dans le dossier
            if f not in self.music_files and os.path.isfile(f):
                self.music_files.append(f)

    # Méthode ajoutant un dossier
    def add_folder(self, folder: str):
        """
        Ajoute tous les fichiers audio d'un dossier (non récursif).

        Args:
            folder (str): Chemin du dossier à ajouter.
        """
        # Vérification de la présence du dossier
        if not folder or not os.path.isdir(folder):
            return
        # Itération des composants du dossier
        for file in os.listdir(folder):
            # Vérification d'ajout du dossier (extension)
            if file.lower().endswith(self.SUPPORTED_EXTENSIONS):
                full_path = os.path.join(folder, file)
                # Vérificaiton de la présence du dossier
                if full_path not in self.music_files:
                    self.music_files.append(full_path)
    
    # Méthode qui élimine un fichier
    def remove_file(self, path: str):
        """
        Supprime un fichier de la bibliothèque s'il est présent.

        Args:
            path (str): Chemin du fichier à supprimer.
        """
        # Vérification du chemin dans le dossier des musiques
        if path in self.music_files:
            self.music_files.remove(path)
            
    # Méthode qui efface la bibliothèque     
    def clear(self):
        """Vide complètement la bibliothèque musicale."""
        self.music_files.clear()
        
        
    # =======================
    # Preview / lecture
    # =======================
    
    # Méthode qui lance la lecture
    def preview(self, file_path: str):
        """
        Lance la lecture d'un fichier audio.

        Args:
            file_path (str): Chemin du fichier à jouer.
        """
        if not file_path or not os.path.exists(file_path):
            return
        
        # Stopper la lecture en cours si nécessaire
        if self.player.playbackState() == QMediaPlayer.PlaybackState.PlayingState:
            self.player.stop()
        
        # Chemin du fichier qui est lu
        qurl = QUrl.fromLocalFile(file_path)
        
        # Affichage du chemin du fichier
        self.player.setSource(qurl)
        
        # Volume standard, peut être exposé si besoin
        self.audio_output.setVolume(0.6)
        # Instanciation du bouton LECTURE
        self.player.play()
        
    # Méthode d'arrêt de la lecture
    def stop_preview(self):
        """Arrête la lecture en cours si elle est active."""
        if self.player.playbackState() != QMediaPlayer.PlaybackState.StoppedState:
            # Instanciation du bouton STOP
            self.player.stop()
    
    
    def toggle_play_pause(self):
        """Alterne entre lecture et pause selon l'état actuel du player."""
        state = self.player.playbackState()
        # condition pour la pause
        if state == QMediaPlayer.PlaybackState.PlayingState:
            self.player.pause()
        else:
            self.player.play()    