import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.slider1 = QSlider()			            # 1
        self.slider1.setRange(0, 99)
        self.slider1.setValue(66)
        self.slider1.setSingleStep(2)
        self.slider1.valueChanged.connect(self.show_value)

        self.slider2 = QSlider()			            # 2
        self.slider2.setOrientation(Qt.Horizontal)
        self.slider2.setMinimum(0)
        self.slider2.setMaximum(99)

        self.slider3 = QSlider(Qt.Horizontal)
        self.slider3.setRange(0, 99)
        self.slider3.setTickPosition(QSlider.TicksBelow)    # 3
        self.slider3.setTickInterval(10)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.slider1)
        v_layout.addWidget(self.slider2)
        v_layout.addWidget(self.slider3)
        self.setLayout(v_layout)

    def show_value(self):
        print(self.slider1.value())


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())