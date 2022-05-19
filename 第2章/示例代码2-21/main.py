import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.dial = QDial()
        self.dial.setRange(0, 365)				        # 1
        self.dial.valueChanged.connect(self.show_value)
        self.dial.setNotchesVisible(True)			    # 2
        self.dial.setNotchTarget(10.5)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.dial)
        self.setLayout(h_layout)

    def show_value(self):
        print(self.dial.value())


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())