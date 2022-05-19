import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(400, 400)
        self.move(0, 0)			    # 1

        self.edit = QTextEdit(self)
        self.edit.move(0, 0)		# 2

        self.btn = QPushButton('button', self.edit)
        self.btn.move(20, 20)		# 3


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())