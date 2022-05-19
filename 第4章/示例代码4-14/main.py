import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(300, 300)

        self.btn1 = QPushButton('移动', self)	# 1
        self.btn2 = QPushButton('更新', self)	# 2
        self.btn1.move(0, 0)
        self.btn2.move(50, 50)
        self.btn1.clicked.connect(lambda: self.btn1.move(100, 100))
        self.btn2.clicked.connect(self.update)

    def paintEvent(self, event):			    # 3
        print('paint')
        print(event.rect())


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())