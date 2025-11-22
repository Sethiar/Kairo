from PyQt6.QtWidgets import QComboBox, QListView, QLineEdit
from app.styles.style_manager import StyleManager



class CustomLineEdit(QLineEdit):
    def __init__(self, width=250, parent=None):
        super().__init__(parent)
        self.setFixedWidth(width)
        self.setStyleSheet(f"""
            padding: 6px 8px;
            font-size: {StyleManager.get('FONT_SIZE_SETTINGS')};
            background-color: {StyleManager.get('BG_INPUT')};
            border-radius: {StyleManager.get('BORDER_RADIUS_BTN')};
            border: 1px solid {StyleManager.get('LINE_SETTING_COLOR')};
        """)
        
        
class CustomComboBox(QComboBox):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Récupération des styles depuis StyleManager
        font_size = StyleManager.get("FONT_SIZE_SETTINGS")
        bg = StyleManager.get("BACKGROUND_COLOR")
        border = StyleManager.get("BORDER_COLOR")
        radius = StyleManager.get("BORDER_RADIUS_BTN")
        text_color = StyleManager.get("TEXT_COLOR_2")
        hover_bg = StyleManager.get("BUTTON_FG_HOVER")
        selected_item = StyleManager.get("DISABLED_COLOR")

        self.setMaximumWidth(180)

        # ----------------------
        # Menu déroulant (QListView)
        # ----------------------
        view = QListView()
        view.setStyleSheet(f"""
            background-color: {bg};
            border: 1px solid {border};
            border-radius: {radius};
            selection-background-color: {hover_bg};
            selection-color: {text_color};
            padding: 4px;
        """)
        self.setView(view)

        # ----------------------
        # Style du QComboBox principal
        # ----------------------
        self.setStyleSheet(f"""
            QComboBox {{
                font-size: {font_size};
                padding: 6px 30px 6px 10px; /* espace pour la flèche externe */
                background-color: {bg};
                border: 1px solid {border};
                border-radius: {radius};
            }}

            /* Masque la flèche native */
            QComboBox::drop-down {{
                width: 0px;
                border: none;
            }}

            /* Items du menu */
            QComboBox QAbstractItemView::item {{
                padding: 8px 10px;
                font-size: {font_size};
                min-height: {int(font_size.replace("px", "")) + 10}px;
                border-radius: {radius};
            }}
            
            /* Items du menu */
            QComboBox QAbstractItemView::viewport {{
                background-color: transparent;
            }}

            QComboBox QAbstractItemView::item:selected {{
                background-color: {selected_item};
                color: {text_color};
                border-radius: {radius};
            }}
        """)