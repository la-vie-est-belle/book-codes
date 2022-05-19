import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(300, 300)

        self.brush1 = QBrush()                              # 1
        self.brush1.setColor(Qt.red)
        self.brush1.setStyle(Qt.Dense6Pattern)

        gradient = QLinearGradient(100, 100, 200, 200)      # 2
        gradient.setColorAt(0.3, QColor(255, 0, 0))
        gradient.setColorAt(0.6, QColor(0, 255, 0))
        gradient.setColorAt(1.0, QColor(0, 0, 255))
        self.brush2 = QBrush(gradient)

        self.brush3 = QBrush()                              # 3
        self.brush3.setTexture(QPixmap('smile.png'))

    def paintEvent(self, event):				            # 4
        painter = QPainter(self)
        painter.setBrush(self.brush1)
        painter.drawRect(0, 0, 100, 100)

        painter.setBrush(self.brush2)
        painter.drawRect(100, 100, 100, 100)

        painter.setBrush(self.brush3)
        painter.drawRect(200, 200, 100, 100)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())