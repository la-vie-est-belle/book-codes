import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import qdarkstyle


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.btn = QPushButton('button', self)


if __name__ == '__main__':
    app = QApplication([])
    qss = qdarkstyle.load_stylesheet()
    app.setStyleSheet(qss)

    window = Window()
    window.show()
    sys.exit(app.exec())