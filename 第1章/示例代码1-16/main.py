import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.btn = QPushButton('Start', self)
        self.btn.clicked.connect(self.change_text)		# 1
        self.btn.clicked.connect(self.change_size)

    def change_text(self):
        if self.btn.text() == 'Start':
            self.btn.setText('Stop')
        else:
            self.btn.setText('Start')

    def change_size(self):				                # 2
        self.btn.resize(150, 30)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())