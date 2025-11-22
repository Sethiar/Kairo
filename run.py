"""
Fichier de démarrage du logiciel - Kairo.

Auteur : SethiarWorks
Date : 01-12-2025


Description :

Ce module intiailise et lance le logiciel Kairo en cr&éant une instance
de QApplication et en affichant la fenêtre principale défiie dans Kairo/

Il importe aussi les modules nécessaires pour la gestion de l'interface 
utiisateur avec PyQt6
"""

import sys
import traceback

from PyQt6.QtWidgets import QApplication

from app.ui.main_window import MainWindow

# Définition de la méthode afin de lancer l'application codée.=
def main():
    try:
        app = QApplication(sys.argv)
        main_window = MainWindow()
        main_window.show()
        sys.exit(app.exec())
    except Exception as e:
        print("Une erreur est survenue :")
        traceback.print_exc()
    
# Lancement de l'instance    
if __name__ == "__main__":
    main()
        
    