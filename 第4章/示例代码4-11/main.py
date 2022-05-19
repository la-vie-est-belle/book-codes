import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setMouseTracking(True)		    # 1

    def mousePressEvent(self, event):		# 2
        if event.button() == Qt.LeftButton:
            print('鼠标左键')
        elif event.button() == Qt.MiddleButton:
            print('鼠标中键')
        elif event.button() == Qt.RightButton:
            print('鼠标右键')

    def mouseMoveEvent(self, event):		# 3
        print(event.pos())
        print(event.globalPos())

    def mouseReleaseEvent(self, event):		# 4
        print('释放')

    def mouseDoubleClickEvent(self, event): # 4
        print('双击')


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())