import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.button = QPushButton('点我')
        self.button.clicked.connect(self.change_text)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.button)
        self.setLayout(h_layout)

    def change_text(self):	    # 1
        choice = QMessageBox.question(self, '询问框', '是否改变文本？',
                                      QMessageBox.Yes | QMessageBox.No)
        if choice == QMessageBox.Yes:
            self.button.setText('文本改变')


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())