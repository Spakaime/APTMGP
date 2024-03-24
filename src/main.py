import sys
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *

class Home_View(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("APT MGP")
        self.setGeometry(100, 100, 1600, 900)

        # Main widget
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)
        
        # Vertical layout for main widget
        self.QVlayout = QVBoxLayout()
        self.main_widget.setLayout(self.QVlayout)

        # Header widget
        self.header_widget = QWidget()
        self.header_layout = QHBoxLayout()
        self.header_widget.setLayout(self.header_layout)
        self.header_label = QLabel("APT MGP")
        self.header_layout.addWidget(self.header_label)
        self.QVlayout.addWidget(self.header_widget)

        # Body widget
        self.body_widget = QWidget()
        self.body_layout = QHBoxLayout()
        self.body_widget.setLayout(self.body_layout)
        self.left_widget = QWidget()
        self.left_layout = QVBoxLayout()
        self.left_widget.setLayout(self.left_layout)
        self.right_widget = QWidget()
        self.right_layout = QVBoxLayout()
        self.right_widget.setLayout(self.right_layout)
        
        # Add widgets to left and right layouts
        self.left_label = QLabel("Left Widget")
        self.left_layout.addWidget(self.left_label)
        
        self.right_label = QLabel("Right Widget")
        self.right_layout.addWidget(self.right_label)
        
        # Add left and right widgets to body layout
        self.body_layout.addWidget(self.left_widget)
        self.body_layout.addWidget(self.right_widget)

        # Form widget
        self.form_widget = QWidget()
        self.form_layout = QFormLayout()
        self.form_widget.setLayout(self.form_layout)
        
        # Add form fields to form layout
        self.file_label = QLabel("File:")
        self.file_edit = QLineEdit()
        
        self.code_label = QLabel("Code UE:")
        self.code_edit = QLineEdit()
        
        self.note_label = QLabel("Note:")
        self.note_edit = QLineEdit()
        
        self.credit_label = QLabel("Credit:")
        self.credit_edit = QLineEdit()
        
        # Add form fields to form layout
        self.form_layout.addRow(self.file_label, self.file_edit)
        self.form_layout.addRow(self.code_label, self.code_edit)
        self.form_layout.addRow(self.note_label, self.note_edit)
        self.form_layout.addRow(self.credit_label, self.credit_edit)

        # Add widgets to main layout
        self.QVlayout.addWidget(self.body_widget)
        self.QVlayout.addWidget(self.form_widget)
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = Home_View()
    view.show()
    sys.exit(app.exec())
