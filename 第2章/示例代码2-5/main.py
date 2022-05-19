import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        button = QPushButton('信息框')			# 1
        button.clicked.connect(self.show_information)

        h_layout = QHBoxLayout()
        h_layout.addWidget(button)
        self.setLayout(h_layout)

    def show_information(self):				    # 2
        QMessageBox.information(self, '标题', '内容', QMessageBox.Yes)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())