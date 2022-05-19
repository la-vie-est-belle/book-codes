import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.browser = QTextBrowser()
        self.button = QPushButton('新增一行')
        self.button.clicked.connect(self.append_text)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.browser)
        v_layout.addWidget(self.button)
        self.setLayout(v_layout)

    def append_text(self):
        self.browser.append('+1')


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())