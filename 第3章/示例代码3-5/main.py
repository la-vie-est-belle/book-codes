import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.scroll_area = QScrollArea()

        self.pic_label = QLabel()
        self.pic_label.setPixmap(QPixmap('pyqt.jpg'))
        self.scroll_area.setWidget(self.pic_label)

        self.scroll_bar = QScrollBar()
        self.scroll_bar.setOrientation(Qt.Horizontal)
        self.scroll_area.setHorizontalScrollBar(self.scroll_bar)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.scroll_area)
        v_layout.addWidget(self.scroll_bar)
        self.setLayout(v_layout)
        

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())