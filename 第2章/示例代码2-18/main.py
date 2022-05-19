import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.lcd1 = QLCDNumber()
        self.lcd1.setDigitCount(5)					            # 1
        self.lcd1.display(12345)					            # 2
        self.lcd1.setMode(QLCDNumber.Hex)				        # 3

        self.lcd2 = QLCDNumber()
        self.lcd2.setDigitCount(5)
        self.lcd2.display(0.1234)
        self.lcd2.setSegmentStyle(QLCDNumber.Flat)			    # 4

        self.lcd3 = QLCDNumber()
        self.lcd3.setDigitCount(5)
        self.lcd3.display(123456789)
        self.lcd3.overflow.connect(lambda: print('overflow')) 	# 5

        self.lcd4 = QLCDNumber()
        self.lcd4.display('HELLO')					            # 6

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.lcd1)
        v_layout.addWidget(self.lcd2)
        v_layout.addWidget(self.lcd3)
        v_layout.addWidget(self.lcd4)
        self.setLayout(v_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())