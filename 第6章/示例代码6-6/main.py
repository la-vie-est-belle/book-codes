import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.label = QLabel('0')
        self.label.setAlignment(Qt.AlignCenter)
        self.btn = QPushButton('计数')
        self.btn.clicked.connect(self.count)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.label)
        v_layout.addWidget(self.btn)
        self.setLayout(v_layout)

    def count(self):			# 1
        num = 0
        while num < 10000000:
            num += 1
            self.label.setText(str(num))
            

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())