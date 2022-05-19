import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.check_box1 = QCheckBox('Check 1')
        self.check_box2 = QCheckBox('Check 2')
        self.check_box3 = QCheckBox('Check 3')

        self.check_box1.setChecked(True)				        # 1
        self.check_box2.setChecked(False)
        self.check_box3.setTristate(True)
        self.check_box3.setCheckState(Qt.PartiallyChecked)

        self.check_box1.stateChanged.connect(self.show_state)	# 2
        self.check_box2.stateChanged.connect(self.show_state)
        self.check_box3.stateChanged.connect(self.show_state)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.check_box1)
        v_layout.addWidget(self.check_box2)
        v_layout.addWidget(self.check_box3)
        self.setLayout(v_layout)

    def show_state(self):
        print(self.sender().checkState())


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())