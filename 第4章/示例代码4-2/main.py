import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QLineEdit):
    def __init__(self):
        super(Window, self).__init__()
        self.btn = QPushButton('button')

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.btn)
        self.setLayout(h_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())