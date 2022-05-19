import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(300, 300)
        self.status_bar = QStatusBar()		    # 1
        self.setStatusBar(self.status_bar)

        self.btn = QPushButton('保存', self)
        self.btn.clicked.connect(self.save)

    def save(self):
        self.status_bar.showMessage('已保存')	# 2


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())