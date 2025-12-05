# app/ui/menu/menu_button.py

"""
Module menu_button
------------------

Contient la classe MenuButton, un bouton personnalisé utilisé dans le menu
latéral de l'application Kairo.

Ce widget :
- émet un signal contenant un ID d'écran (screen_id)
- applique un style réactif aux thèmes et au scale des polices
- met à jour dynamiquement sa taille de police lorsque le thème change
- possède un mode "actif" visuellement distinct


Auteur : SethiarWorks
Date : 01-01-2026
"""
from PyQt6.QtWidgets import QPushButton
from PyQt6.QtCore import pyqtSignal

from app.styles.style_manager import StyleManager
from app.core.settings.theme_manager import ThemeManager


class MenuButton(QPushButton):
    """
    Bouton personnalisé utilisé dans le menu latéral.

    Attributs
    ---------
    clicked_with_id : pyqtSignal(str)
        Signal émis lorsque le bouton est cliqué, transmet son screen_id.
    screen_id : str
        Identifiant permettant au contrôleur de savoir quelle vue afficher.
    active : bool
        Indique si le bouton est l’onglet actif dans le menu.
    """
    
    clicked_with_id = pyqtSignal(str)
    
    def __init__(self, text, screen_id, parent=None):
        """
        Initialise un bouton de menu.

        Parameters
        ----------
        text : str
            Texte affiché sur le bouton.
        screen_id : str
            Identifiant unique de l'écran associé.
        parent : QWidget, optional
            Widget parent.
        """
        super().__init__(text, parent)
        self.screen_id = screen_id
        self.active = False
        
        # Chargement initial du style
        self._apply_base_style()
        
        # Click -> émettre screen_id
        self.clicked.connect(self._emit_id)
        
        # Mise à jour automatique lors d’un changement de thème / scale
        ThemeManager.get_instance().theme_changed.connect(self._update_font_scale)
    
    
    # =======================
    # SIGNALS & INTERACTIONS
    # =======================  
        
    def _emit_id(self):
        """Émet le signal clicked_with_id avec l'ID de l'écran."""
        self.clicked_with_id.emit(self.screen_id)
        
        
    # =======================
    # STYLE MANAGEMENT
    # ======================= 
    def _update_font_scale(self):
        """
        Met à jour la taille de police du bouton selon le scale actuel.
        Appelé automatiquement lors d'un changement de thème.
        """
        font_size = StyleManager.get_scaled_font("FONT_SIZE_BULLET")
        self.setStyleSheet(
            self._base_style_template.format(
                font_size=font_size, 
                active=self.active
            )
        )
               
    
    def _apply_base_style(self):
        """
        Charge le style par défaut du bouton (mode inactif).
        """
        font_size = StyleManager.get_scaled_font("FONT_SIZE_BULLET")
        self.active = False
        self._base_style_template = """
            QPushButton {{
                padding: 12px 20px;
                border-radius: 10px;
                font-size: {font_size};
                font-weight: 600;
                color: white;
                background: transparent;
            }}
            QPushButton:hover {{
                background: #33475B;
            }}
        """
        self.setStyleSheet(
            self._base_style_template.format(
                font_size=font_size, 
                active=False
            )
        )         

    
    
    def set_active(self, is_active: bool):
        """
        Change l'état visuel du bouton (actif / normal).

        Parameters
        ----------
        is_active : bool
            True pour activer l'effet "sélectionné", False pour revenir au style normal.
        """
        self.active = is_active
        font_size = StyleManager.get_scaled_font("FONT_SIZE_BULLET")
        if is_active:
            style = """
                QPushButton {{
                    padding: 12px 20px;
                    border-radius: 12px;
                    font-size: {font_size};
                    font-weight: 700;
                    color: #FFF;
                    background: #1B2838;
                }}
            """.format(font_size=font_size)
            self.setStyleSheet(style)
        else:
            self._apply_base_style()