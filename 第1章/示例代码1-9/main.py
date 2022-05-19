import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        username_label = QLabel('Username:')		    # 1
        password_label = QLabel('Password:')
        username_line = QLineEdit()
        password_line = QLineEdit()

        f_layout = QFormLayout()				        # 2
        f_layout.addRow(username_label, username_line)
        f_layout.addRow(password_label, password_line)
        self.setLayout(f_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())