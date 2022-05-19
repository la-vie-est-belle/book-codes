import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.btn = QPushButton('Start', self)
        self.btn.pressed.connect(self.change_text)		# 1
        self.btn.released.connect(self.change_text)

    def change_text(self):
        if self.btn.text() == 'Start':
            self.btn.setText('Stop')
        else:
            self.btn.setText('Start')

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
sys.exit(app.exec())