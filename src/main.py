import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QFrame
from PyQt6.QtGui import QPainter, QPen
from PyQt6.QtCore import Qt

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

class Home_View(QMainWindow):
    def __init__(self):
        super().__init__()

        self.interface()

    def interface(self):
        self.setWindowTitle("APT MGP")
        self.setGeometry(100, 100, 900, 800)

        # Création du QFrame
        frame = CustomFrame(self)
        frame.setGeometry(self.width() // 4 - 1, 0, 2, self.height())

        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    home = Home_View()
    sys.exit(app.exec())