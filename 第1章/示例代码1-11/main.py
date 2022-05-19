import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        username_label = QLabel('Username:')
        password_label = QLabel('Password:')
        username_line = QLineEdit()
        password_line = QLineEdit()

        v_layout = QVBoxLayout()					# 1
        h1_layout = QHBoxLayout()
        h2_layout = QHBoxLayout()
        h1_layout.addWidget(username_label)
        h1_layout.addWidget(username_line)
        h2_layout.addWidget(password_label)
        h2_layout.addWidget(password_line)
        v_layout.addLayout(h1_layout)
        v_layout.addLayout(h2_layout)
        self.setLayout(v_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())