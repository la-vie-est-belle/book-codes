import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.button = QPushButton('demo', self)
        self.button.setIcon(QIcon('button.png'))	# 1
        self.button.setFlat(True)			        # 2
        self.button.clicked.connect(lambda: self.button.setEnabled(False))  # 3

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.button)
        self.setLayout(h_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())