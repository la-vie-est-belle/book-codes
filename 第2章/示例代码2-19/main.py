import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.spinbox = QSpinBox()		    # 1
        self.spinbox.setRange(-99, 99)
        self.spinbox.setSingleStep(2)
        self.spinbox.setValue(66)
        self.spinbox.valueChanged.connect(self.show_spinbox_value)

        self.db_spinbox = QDoubleSpinBox()	# 2
        self.db_spinbox.setRange(-99.99, 99.99)
        self.db_spinbox.setSingleStep(1.5)
        self.db_spinbox.setValue(66.66)
        self.db_spinbox.valueChanged.connect(self.show_db_spinbox_value)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.spinbox)
        v_layout.addWidget(self.db_spinbox)
        self.setLayout(v_layout)

    def show_spinbox_value(self):
        print(self.spinbox.value())

    def show_db_spinbox_value(self):
        print(self.db_spinbox.value())


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())