import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(200, 200)			            # 1

        desktop = QApplication.desktop()
        desktop_width = desktop.width()
        desktop_height = desktop.height()

        window_width = self.frameSize().width()	    # 2
        window_height = self.frameSize().height()

        x = desktop_width // 2 - window_width // 2
        y = desktop_height // 2 - window_height // 2
        self.move(x, y)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())