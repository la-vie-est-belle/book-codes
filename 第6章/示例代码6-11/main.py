import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(300, 300)

        self.pen = QPen()                       # 1
        self.pen.setWidth(5)
        self.pen.setColor(Qt.black)
        self.pen.setStyle(Qt.DashLine)
        self.pen.setCapStyle(Qt.RoundCap)
        self.pen.setJoinStyle(Qt.MiterJoin)

    def paintEvent(self, event):			    # 2
        painter = QPainter(self)
        painter.setPen(self.pen)
        painter.drawLine(20, 20, 280, 280)
        painter.drawRect(20, 20, 260, 260)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())