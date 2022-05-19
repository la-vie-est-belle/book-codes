import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        label = QLabel()
        text = 'I like PyQt.'
        words = text.split(' ')		# 1
        label.setText('\n'.join(words))

        h_layout = QHBoxLayout()
        h_layout.addWidget(label)
        self.setLayout(h_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())