import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt
from views.home_view import home_View

class CustomFrame(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAutoFillBackground(True)

    def paintEvent(self, event):
        painter = QPainter(self)
        pen = QPen(Qt.GlobalColor.black)
        pen.setWidth(1)
        painter.setPen(pen)
        x = self.width() // 4
        painter.drawLine(x, 0, x, self.height())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = Home_View()
    view.show()
    sys.exit(app.exec())

