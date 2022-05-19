import sys
from PyQt5.QtWidgets import *


class Window(QWidget):				            # 1
    def __init__(self):
        super(Window, self).__init__()
        label_1 = QLabel('Label 1', self)		# 2
        label_2 = QLabel('Label 2', self)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()				            # 3
    window.show()
    sys.exit(app.exec())