import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowOpacity(0.8)                      # 1
        self.setWindowFlag(Qt.FramelessWindowHint)      # 2
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.another_window = AnotherWindow()

        self.btn = QPushButton('显示另一个窗口')
        self.btn.clicked.connect(self.another_window.show)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.btn)
        self.setLayout(h_layout)


class AnotherWindow(QWidget):
    def __init__(self):
        super(AnotherWindow, self).__init__()
        self.setWindowModality(Qt.ApplicationModal)  # 3


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())