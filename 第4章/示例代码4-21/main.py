import sys
import time
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

    def load(self, splash):
        for i in range(101):
            time.sleep(0.05)
            splash.showMessage(f'加载 {i}%', Qt.AlignBottom|Qt.AlignCenter)


if __name__ == '__main__':
    app = QApplication([])

    splash = QSplashScreen()
    splash.setPixmap(QPixmap('qt.png'))	# 1
    splash.show()
    splash.showMessage('加载 0%', Qt.AlignBottom|Qt.AlignCenter)

    window = Window()
    window.load(splash)
    window.show()				        # 2
    splash.finish(window)
    sys.exit(app.exec())