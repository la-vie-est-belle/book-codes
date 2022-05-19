import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from qt_material import apply_stylesheet


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.btn = QPushButton('button', self)


if __name__ == '__main__':
    app = QApplication([])
    apply_stylesheet(app, theme='dark_teal.xml')    # 1

    window = Window()
    window.show()
    sys.exit(app.exec())