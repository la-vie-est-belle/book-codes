import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.btn = QPushButton('Start', self)
        self.btn.clicked.connect(self.change_text)		# 1

    def change_text(self):				                # 2
        if self.btn.text() == 'Start':
            self.btn.setText('Stop')
        else:
            self.btn.setText('Start')


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())