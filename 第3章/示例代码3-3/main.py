import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.pic_scroll_area = QScrollArea()        # 1
        self.btn_scroll_area = QScrollArea()

        pic_label = QLabel()
        pic_label.setPixmap(QPixmap('pyqt.jpg'))
        self.pic_scroll_area.setWidget(pic_label)   # 2
        self.pic_scroll_area.ensureVisible(750, 750, 100, 100)

        widget_for_btns = QWidget()                 # 3
        btn_h_layout = QHBoxLayout()
        for i in range(100):
            btn = QPushButton(f'按钮{i+1}')
            btn_h_layout.addWidget(btn)
        widget_for_btns.setLayout(btn_h_layout)
        self.btn_scroll_area.setWidget(widget_for_btns)
        self.btn_scroll_area.setAlignment(Qt.AlignCenter)

        window_v_layout = QVBoxLayout()
        window_v_layout.addWidget(self.pic_scroll_area)
        window_v_layout.addWidget(self.btn_scroll_area)
        self.setLayout(window_v_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())