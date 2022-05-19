import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.bulb_pic = QLabel()				            # 1
        self.bulb_pic.setPixmap(QPixmap('bulb-off.png'))

        self.radio_btn1 = QRadioButton('关')		        # 2
        self.radio_btn2 = QRadioButton('开')
        self.radio_btn1.setChecked(True)
        self.radio_btn1.toggled.connect(self.turn_off)	    # 3
        self.radio_btn2.toggled.connect(self.turn_on)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.bulb_pic)
        h_layout.addWidget(self.radio_btn1)
        h_layout.addWidget(self.radio_btn2)
        self.setLayout(h_layout)

    def turn_off(self):
        self.bulb_pic.setPixmap(QPixmap('bulb-off.png'))

    def turn_on(self):
        self.bulb_pic.setPixmap(QPixmap('bulb-on.png'))


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())