import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        username_label = QLabel('Username:')
        password_label = QLabel('Password:')
        username_line = QLineEdit()
        password_line = QLineEdit()

        g_layout = QGridLayout()			        # 1
        g_layout.addWidget(username_label, 0, 0)
        g_layout.addWidget(username_line, 0, 1)
        g_layout.addWidget(password_label, 1, 0)
        g_layout.addWidget(password_line, 1, 1)
        self.setLayout(g_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())