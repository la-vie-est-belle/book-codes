import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import*


class Window(QWidget):
    my_signal = pyqtSignal()			        # 1

    def __init__(self):
        super(Window, self).__init__()
        self.my_signal.connect(self.my_slot)	# 2

    def my_slot(self):
        print(self.width())
        print(self.height())

    def mousePressEvent(self, event):		    # 3
        self.my_signal.emit()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())