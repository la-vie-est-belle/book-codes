import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        username_label = QLabel('Username:')	# 1
        username_line = QLineEdit()

        h_layout = QHBoxLayout()			    # 2
        h_layout.addWidget(username_label)
        h_layout.addWidget(username_line)
        self.setLayout(h_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())