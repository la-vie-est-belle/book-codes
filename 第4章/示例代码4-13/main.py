import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QLabel):				        # 1
    def __init__(self):
        super(Window, self).__init__()
        self.resize(300, 300)
        self.setAcceptDrops(True)			# 2

    def dragEnterEvent(self, event):		# 3
        print('进入')
        if event.mimeData().hasUrls():
            event.accept()

    def dragMoveEvent(self, event):		    # 4
        print('移动')

    def dragLeaveEvent(self, event):
        print('离开')

    def dropEvent(self, event):			    # 5
        print('放下')
        url = event.mimeData().urls()[0]
        file_path = url.toLocalFile()
        if file_path.endswith('.png'):
            self.setPixmap(QPixmap(file_path))
            self.setAlignment(Qt.AlignCenter)
            self.setScaledContents(True)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())