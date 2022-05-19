import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        btn = QPushButton('Start', self)
        btn.clicked.connect(lambda: btn.setText('Stop'))	# 1


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())