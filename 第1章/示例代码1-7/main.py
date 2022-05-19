import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        username = QLabel('Username:')		# 1
        password = QLabel('Password:')

        v_layout = QVBoxLayout()			# 2
        v_layout.addWidget(username)
        v_layout.addWidget(password)
        self.setLayout(v_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())