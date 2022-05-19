import sys
from PyQt5.QtWidgets import *


if __name__ == '__main__':
    app = QApplication([])
    label_1 = QLabel('Label 1')
    label_2 = QLabel('Label 2')
    label_1.show()
    label_2.show()
    sys.exit(app.exec())