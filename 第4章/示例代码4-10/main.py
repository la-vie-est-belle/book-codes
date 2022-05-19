import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

    def keyPressEvent(self, event):	    # 1
        if event.key() == Qt.Key_A:
            print('a')
        if event.text().lower() == 'b':
            print('b')
        if event.modifiers()==Qt.ShiftModifier and event.key()==Qt.Key_Q:
            print('shift+q')

    def keyReleaseEvent(self, event):
        print(event.key())
        print(event.text())


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())