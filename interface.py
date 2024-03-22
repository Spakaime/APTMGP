import sys
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calcul MGP")
        self.setMinimumSize(QSize(800, 580))
    	
        # self.logo_label = QLabel()
        # self.logo_label.setPixmap(QPixmap("logo.png"))
        
        try:
            with open("style.qss", "r") as style_file:
                style_sheet = style_file.read()
                app.setStyleSheet(style_sheet)
        except FileNotFoundError:
            print("Error: Could not find stylesheet 'styles.qss'")
        	
        # Création des widgets principaux
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout()
        self.main_widget.setLayout(self.layout)

        # **En-tête**
        self.header_widget = QWidget()
        self.header_layout = QHBoxLayout()
        self.header_widget.setLayout(self.header_layout)

        self.logo_label = QLabel()
        self.logo_label.setPixmap(QPixmap("logo.png"))
        self.header_layout.addWidget(self.logo_label)

        self.title_label = QLabel("Calcul MGP")
        self.title_label.setFont(QFont("Arial", 18))
        self.header_layout.addWidget(self.title_label)

        self.layout.addWidget(self.header_widget)

        # **Onglets**
        self.tab_widget = QTabWidget()
        self.layout.addWidget(self.tab_widget)

        # **Onglet "Ajouter vos notes"**
        self.add_notes_tab = QWidget()
        self.tab_widget.addTab(self.add_notes_tab, "Ajouter vos notes")

        self.add_notes_layout = QVBoxLayout()
        self.add_notes_tab.setLayout(self.add_notes_layout)

        # **Section UE**
        self.ue_section_widget = QWidget()
        self.ue_section_layout = QHBoxLayout()
        self.ue_section_widget.setLayout(self.ue_section_layout)

        self.ue_label = QLabel("Nom de l'UE :")
        self.ue_section_layout.addWidget(self.ue_label)

        self.ue_name_edit = QLineEdit()
        self.ue_section_layout.addWidget(self.ue_name_edit)

        self.credit_label = QLabel("Crédits :")
        self.ue_section_layout.addWidget(self.credit_label)

        self.credit_edit = QLineEdit()
        self.ue_section_layout.addWidget(self.credit_edit)

        self.add_notes_layout.addWidget(self.ue_section_widget)

        # **Section Note**
        self.note_section_widget = QWidget()
        self.note_section_layout = QHBoxLayout()
        self.note_section_widget.setLayout(self.note_section_layout)

        self.note_label = QLabel("Note :")
        self.note_section_layout.addWidget(self.note_label)

        self.note_edit = QLineEdit()
        self.note_section_layout.addWidget(self.note_edit)

        self.add_notes_layout.addWidget(self.note_section_widget)

        # **Bouton Valider**
        self.validate_button = QPushButton("Valider")
        self.add_notes_layout.addWidget(self.validate_button)

        # **Onglet "Résultat"**
        self.result_tab = QWidget()
        self.tab_widget.addTab(self.result_tab, "Résultat")

        self.result_layout = QVBoxLayout()
        self.result_tab.setLayout(self.result_layout)

        # **Label MGP**
        self.mgp_label = QLabel("MGP :")
        self.mgp_label.setFont(QFont("Arial", 18))
        self.result_layout.addWidget(self.mgp_label)

        # **Affichage MGP**
        self.mgp_value_label = QLabel()
        self.mgp_value_label.setFont(QFont("Arial", 24))
        self.result_layout.addWidget(self.mgp_value_label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    sys.exit()
    