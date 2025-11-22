"""
VARS_COLORS
===========

Dictionnaire contenant toutes les variables de couleur utilisées par l'application.
Ces valeurs constituent les “design tokens” du thème visuel.

Chaque couleur doit être :
- explicitement nommée (noms fonctionnels, jamais des noms visuels : pas “light_grey”)
- centralisée ici pour éviter toute duplication
- utilisée uniquement via le StyleManager (ou import direct si nécessaire)

Exemples d’usage :
------------------

Dans un stylesheet Python :

    color = StyleManager.get("TEXT_COLOR_1")

Dans un widget PyQt :

    widget.setStyleSheet(f"background-color: {StyleManager.get('PRIMARY_COLOR')};")

Couleurs disponibles :
----------------------

- PRIMARY_COLOR           : Couleur principale du thème (branding)
- SECONDARY_COLOR         : Couleur secondaire (accents secondaires)
- ACCENT_COLOR            : Couleur d'accentuation (actions importantes)
- BACKGROUND_COLOR        : Couleur de fond des pages
- INPUT_BACKGROUND_COLOR  : Fond des champs de saisie
- MENU_BACKGROUND_COLOR   : Fond des menus latéraux
- WIDGET_BACKGROUND_COLOR : Fond des widgets personnalisés
- TEXT_COLOR_1            : Texte clair (titres, éléments contrastés)
- TEXT_COLOR_2            : Texte foncé (paragraphe, contenu standard)
- HOVER_COLOR             : Couleur au survol
- DISABLED_COLOR          : Couleur d'état désactivé
- BORDER_COLOR            : Couleur des bordures

**  Ces couleurs sont utilisées dans les boutons, menus, labels, layouts,
input fields, et widgets personnalisés.

**  Toutes les nouvelles couleurs doivent être ajoutées ici et jamais 
directement dans les styles.

** Rappel : utilisez StyleManager.get("NAME") uniquement, jamais une valeur brute (#xxxxxx)
dans un widget si vous souhaitez garantir la cohérence visuelle et la maintenabilité.
"""


# ============================
# COULEURS
# ============================

VARS_COLORS = {
    
    "Test": "#1F2C3A",
    # Couleurs principales du thème
    "PRIMARY_COLOR": "#E68516",
    "SECONDARY_COLOR": "#E2EE38",
    "ACCENT_COLOR": "#E74C3C",
    
    #--------------------------
    # Couleurs des backgrounds
    #--------------------------
    "BACKGROUND_COLOR": "#FFFFFF",
    "SETTINGS_BG_COLOR": "#D4E0F1F9",
    "MENU_BACKGROUND_COLOR": "#22313F",
    
    
    #---------------------------
    # Couleurs Inputs
    #---------------------------
    # Couleurs de fond des inputs
    "BG_INPUT":"#FFFFFF",

    
    #---------------------------
    # Couleurs des lignes
    #---------------------------
    # Couleurs des lignes des settings
    "LINE_SETTING_COLOR": "#cccccc",
    
    
    #---------------------------
    # Couleurs de fond des boutons des settings
    #---------------------------
    # Couleurs des backgrounds des boutons
    "BTN_SETTING_BG_COLOR": "#85919C",
    "BUTTON_FG": "#ffffff",
    
    # Couleurs de hover des boutons du settings.
    "BTN_SETTING_HOVER_BG_COLOR": "#34495E",
    "BUTTON_FG_HOVER": "#d8c6c6",
    
    
    #--------------------------
    # Couleurs de texte
    #--------------------------
    "TEXT_COLOR_1": "#FFFFFF",
    "TEXT_COLOR_2": "#000000",
    "MENU_TEXT": "#E8EAED",
    
    # Couleurs des textes des settings
    "SETTING_TITLE_COLOR": "#1a1d1f",
    
    
    #--------------------------
    # Couleurs d'état
    #--------------------------
    "DISABLED_COLOR": "#95A5A6",
    
    
    #--------------------------
    # Couleurs des bordures
    #--------------------------
    "LINE_COLOR": "#E9DE4E",
    "BORDER_COLOR": "#2C3E50",
    
    
    #--------------------------
    # Couleurs du menu
    #--------------------------
    "MENU_HOVER_BG": "rgba(255,255,255,0.08)",
    "MENU_ACTIVE_BG": "rgba(255,255,255,0.15)",
    
}