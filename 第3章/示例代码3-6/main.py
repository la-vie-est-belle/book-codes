import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.splitter = QSplitter()

        self.text_edit1 = QTextEdit()
        self.text_edit2 = QTextEdit()
        self.text_edit3 = QTextEdit()
        self.text_edit1.setPlaceholderText('edit 1')
        self.text_edit2.setPlaceholderText('edit 2')
        self.text_edit3.setPlaceholderText('edit 3')

        self.splitter.addWidget(self.text_edit1)		# 1
        self.splitter.insertWidget(0, self.text_edit2)
        self.splitter.addWidget(self.text_edit3)
        self.splitter.setSizes([300, 200, 100])		    # 2
        self.splitter.setOpaqueResize(False)		    # 3

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.splitter)
        self.setLayout(h_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())