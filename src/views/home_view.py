import sys
import PyQt6
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class Home_View(QMainWindow):
    def __init__(self):
        super().__init__()
    
        try:
            with open("/home/mitm/Documents/APTMGP/src/resources/styles/home.qss", "r") as style_file:
                style_sheet = style_file.read()
                app.setStyleSheet(style_sheet)
        except FileNotFoundError:
            print("Error: Could not find stylesheet 'styles.qss'")
        
        self.interface()
     
    def interface(self):    
        # self.setWindowFlag(Qt.WindowType.FramelessWindowHint)
        self.icon = QIcon("/home/mitm/Documents/APTMGP/src/resources/images/logo.jpg")
        self.setWindowIcon(self.icon)
        self.setStyleSheet("""
            QMainWindow::title {
                padding-left: 5px;
                padding-top: 9px;
                background-image: url("chemin/vers/votre/icone.png");
                background-repeat: no-repeat;
                background-position: left center;
            }
        """)
        self.setWindowTitle("APT MGP")
        self.setGeometry(100, 100, 1600, 900)
        
        # ---------( Creation des widgets Principaux )----------
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        
        self.QVlayout = QVBoxLayout()
        self.main_widget.setLayout(self.QVlayout)
        
        self.QVlayout.setContentsMargins(0, 0, 0, 0)
        self.QVlayout.setSpacing(0)

        self.central = QHBoxLayout(self)
        self.frame = QFrame()
        
        # -----------( En-tête )---------
        self.header_widget = QWidget()
        self.header_layout = QHBoxLayout()
        self.header_widget.setLayout(self.header_layout)

        self.pixmap = QPixmap("/home/mitm/Documents/APTMGP/src/resources/images/logo.jpg")

        self.center = QCommandLinkButton(text= "APT MGP", description= "Calculer Votre MGP", icon= QIcon(self.icon))
        self.center.setContentsMargins(0, 0, 0, 0)
        self.center.setIconSize(QSize(self.center.sizeHint()))
        self.center.setFont(QFont("ubuntu", 25)), self.center.setObjectName('com') 
        self.QVlayout.addWidget(self.center)
        # self.QVlayout.addStretch(1)
        
        # --------( Body )-------
        self.body_widget = QWidget()
        self.body_layout = QHBoxLayout(self.body_widget)
        self.QVlayout.addWidget(self.body_widget)

        # Création du QFrame
        self.frame = QFrame(self.body_widget)
        self.frame.setFrameShape(QFrame.Shape.VLine)
        self.body_layout.addWidget(self.frame, alignment=Qt.AlignmentFlag.AlignHCenter)
        self.body_layout.setContentsMargins(700, 5, 10, 10)
        self.body_layout.setSpacing(0)
        self.body_layout.addStretch(1)
        
        # Création du QVBoxLayout pour la partie gauche
        self.left_layout = QHBoxLayout()
        self.body_layout.addLayout(self.left_layout)
        self.left_layout.setAlignment(Qt.AlignmentFlag.AlignTop | Qt.AlignmentFlag.AlignLeft)

        # Création du bouton avec une icône dans la partie gauche
        self.button = QPushButton()
        self.button.setIcon(QIcon("/home/mitm/Documents/APTMGP/src/resources/images/plus_plein.png"))
        self.button.setText("Ajouter")
        self.button_layout = QVBoxLayout()
        self.button_layout.addWidget(self.button)
        self.button.setGeometry(700, 5, 100, 30)
        self.button.move(700, 5)
        self.button_layout.addStretch()
        self.left_layout.addLayout(self.button_layout)
        
        # creation du QVBoxLayout pour la partie droite
        self.right_layout = QFormLayout()
        self.body_layout.addLayout(self.right_layout)
        self.right_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # creation du formulaire pour renseigner comment charger le fichier, le code UE, note et credit
        self.ue_label = QLabel("Code de l'UE :")
        self.ue_name_edit = QLineEdit()
        self.ue_name_edit.setPlaceholderText("Entrez votre nom")

        self.credit_label = QLabel("Crédits :")
        self.credit_edit = QLineEdit()
        self.credit_edit.setPlaceholderText("Entrez le credit")
        
        self.note_label = QLabel("Note /100 :")
        self.note_edit = QLineEdit()
        self.note_edit.setPlaceholderText("Entrez votre note sur 100")

        self.right_layout.addRow(self.ue_label, self.ue_name_edit)
        self.right_layout.addRow(self.credit_label, self.credit_edit)
        self.right_layout.addRow(self.note_label, self.note_edit)
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Home = Home_View()
    Home.show()
    sys.exit(app.exec())