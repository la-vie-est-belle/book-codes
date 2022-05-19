import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.username_line = QLineEdit()		    # 1
        self.password_line = QLineEdit()

        h_layout1 = QHBoxLayout()
        h_layout2 = QHBoxLayout()
        v_layout = QVBoxLayout()
        h_layout1.addWidget(QLabel('Username:'))    # 2
        h_layout1.addWidget(self.username_line)
        h_layout2.addWidget(QLabel('Password:'))
        h_layout2.addWidget(self.password_line)
        v_layout.addLayout(h_layout1)
        v_layout.addLayout(h_layout2)
        self.setLayout(v_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())