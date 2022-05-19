import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.scroll_area = QScrollArea()
        self.original_bar = self.scroll_area.horizontalScrollBar()

        self.pic_label = QLabel()
        self.pic_label.setPixmap(QPixmap('pyqt.jpg'))
        self.scroll_area.setWidget(self.pic_label)

        # 1
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scroll_bar = QScrollBar()				                # 2
        self.scroll_bar.setOrientation(Qt.Horizontal)
        self.scroll_bar.valueChanged.connect(self.move_bar)
        self.scroll_bar.setMinimum(self.original_bar.minimum())
        self.scroll_bar.setMaximum(self.original_bar.maximum())
        # self.scroll_area.setHorizontalScrollBar(self.scroll_bar)	# 3

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.scroll_area)
        v_layout.addWidget(self.scroll_bar)
        self.setLayout(v_layout)

    def move_bar(self):
        value = self.scroll_bar.value()
        self.original_bar.setValue(value)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())