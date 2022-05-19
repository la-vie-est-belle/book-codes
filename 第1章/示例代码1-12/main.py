import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        username_label = QLabel('Username:')
        password_label = QLabel('Password:')
        username_line = QLineEdit()
        password_line = QLineEdit()

        h_layout = QHBoxLayout()
        v1_layout = QVBoxLayout()
        v2_layout = QVBoxLayout()
        v1_layout.addWidget(username_label)
        v1_layout.addWidget(password_label)
        v2_layout.addWidget(username_line)
        v2_layout.addWidget(password_line)
        h_layout.addLayout(v1_layout)
        h_layout.addLayout(v2_layout)
        self.setLayout(h_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())