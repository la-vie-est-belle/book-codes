import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.lcd = QLCDNumber()			# 1
        self.lcd.setSegmentStyle(QLCDNumber.Flat)
        self.lcd.setDigitCount(20)
        self.update_date_time()

        self.timer = QTimer()			# 2
        self.timer.start(1000)
        self.timer.timeout.connect(self.update_date_time)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.lcd)
        self.setLayout(h_layout)

    def update_date_time(self):
        date_time = QDateTime.currentDateTime().toString('yyyy-M-d hh:mm:ss')
        self.lcd.display(date_time)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())