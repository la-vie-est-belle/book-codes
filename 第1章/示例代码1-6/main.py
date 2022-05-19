import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(200, 200)			    # 1

        label_1 = QLabel('Label 1', self)
        label_2 = QLabel('Label 2', self)
        label_1.move(-20, 0)			    # 2
        label_2.move(50, 100)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())