import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.start_x = None
        self.start_y = None

    def mousePressEvent(self, event):		# 1
        if event.button() == Qt.LeftButton:
            self.start_x = event.x()
            self.start_y = event.y()

    def mouseMoveEvent(self, event):		# 2
        dis_x = event.x() - self.start_x
        dis_y = event.y() - self.start_y
        self.move(self.x()+dis_x, self.y()+dis_y)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())