import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.spin_box = QSpinBox(self)
        self.spin_box.resize(100, 30)


if __name__ == '__main__':
    with open('style.qss', 'r', encoding='utf-8') as f:
        qss = f.read()

    app = QApplication([])
    app.setStyleSheet(qss)

    window = Window()
    window.show()
    sys.exit(app.exec())