import sys
from PyQt5.QtWidgets import *


if __name__ == '__main__':
    app = QApplication([])
    label = QLabel()
    label.setText('<h1>Hello, PyQt!</h1>')
    label.show()
    sys.exit(app.exec())