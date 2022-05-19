import sys
from PyQt5.QtWidgets import *


if __name__ == '__main__':
    app = QApplication([])
    label = QLabel()
    with open('test.html', 'r', encoding='utf-8') as f:
        label.setText(f.read())
    label.show()
    sys.exit(app.exec())