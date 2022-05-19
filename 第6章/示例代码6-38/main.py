import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.combo_box = QComboBox()
        self.combo_box.addItems(['English', '中文'])
        self.button = QPushButton()
        self.label = QLabel()
        self.label.setAlignment(Qt.AlignCenter)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.combo_box)
        v_layout.addWidget(self.button)
        v_layout.addWidget(self.label)
        self.setLayout(v_layout)

        self.retranslateUi()

    def retranslateUi(self):             # 1
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate('Window', 'Switch'))
        self.button.setText(_translate('Window', 'Start'))
        self.label.setText(_translate('Window', 'Hello Wrold!'))


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())