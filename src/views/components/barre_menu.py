#________Gradi Joel___________

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *


class barre_menu_(QWidget) :
    def __init__(self, parent: QWidget | None = None) -> None:
        super(barre_menu_, self).__init__(parent)

        self.central  = QVBoxLayout(self)

        self.list_buttons = [
            QPushButton(name) for name in ["View 1", "View 2", "View 3", "View 4"]
        ]

        [[self.central.addWidget(widg), widg.setFixedSize(QSize(150, 35))] for widg in self.list_buttons]

        self.setStyleSheet(open("resources/styles/buttons.css", "r").read())
