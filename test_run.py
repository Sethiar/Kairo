"""
Script de test pour Kairo - MainWindow et ScreenManager
Permet de détecter les erreurs d'initialisation des widgets.
"""

import sys
import traceback
from PyQt6.QtWidgets import QApplication

# Import des modules Kairo
try:
    from app.ui.main_window import MainWindow
except Exception as e:
    print("Erreur lors de l'import de MainWindow :")
    traceback.print_exc()

try:
    from app.ui.screens.screen_manager import ScreenManager
except Exception as e:
    print("Erreur lors de l'import de ScreenManager :")
    traceback.print_exc()

def main():
    try:
        app = QApplication(sys.argv)
        
        print("Création de MainWindow...")
        try:
            main_window = MainWindow()
            main_window.show()
        except Exception as e:
            print("Erreur lors de l'init de MainWindow:")
            traceback.print_exc()
        
        print("Création de ScreenManager séparément...")
        try:
            screen_manager = ScreenManager()
            screen_manager.show()
        except Exception as e:
            print("Erreur lors de l'init de ScreenManager:")
            traceback.print_exc()
        
        sys.exit(app.exec())
    except Exception as e:
        print("Erreur globale QApplication:")
        traceback.print_exc()

if __name__ == "__main__":
    main()