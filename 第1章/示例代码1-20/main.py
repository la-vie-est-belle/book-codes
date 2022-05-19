import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class Window(QWidget):
    my_signal = pyqtSignal(int, int)		# 1

    def __init__(self):
        super(Window, self).__init__()
        self.my_signal.connect(self.my_slot)

    def my_slot(self, x, y):			    # 2
        print(x)
        print(y)

    def mousePressEvent(self, event):		# 3
        x = event.pos().x()
        y = event.pos().y()
        self.my_signal.emit(x, y)

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
sys.exit(app.exec())