import sys
from PyQt5.QtWidgets import *


if __name__ == '__main__':
    app = QApplication([])		    # 1
    label = QLabel('Hello, PyQt!')  # 2
    label.show()				    # 3
    sys.exit(app.exec())		    # 4
