import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.widget = QWidget()			        # 1
        self.edit = QTextEdit()
        self.btn = QPushButton('Button')

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.edit)
        v_layout.addWidget(self.btn)
        self.widget.setLayout(v_layout)

        self.setCentralWidget(self.widget)		# 2


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())