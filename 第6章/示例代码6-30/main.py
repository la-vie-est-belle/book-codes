import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        with open('./style.qss', 'r') as f:
            qss = f.read()
            
        self.btn = QPushButton('button', self)
        self.btn.setStyleSheet(qss)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())