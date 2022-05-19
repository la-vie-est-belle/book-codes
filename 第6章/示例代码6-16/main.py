import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(500, 500)

        self.size_btn = QPushButton('大小', self)
        self.pos_btn = QPushButton('位置', self)
        self.color_btn = QPushButton('颜色', self)
        self.size_btn.move(100, 20)
        self.pos_btn.move(200, 20)
        self.color_btn.move(300, 20)
        self.size_btn.clicked.connect(self.start_anim)
        self.pos_btn.clicked.connect(self.start_anim)
        self.color_btn.clicked.connect(self.start_anim)

        self.size_anim = QPropertyAnimation(self.size_btn, b'size')     # 2
        self.size_anim.setDuration(6000)
        self.size_anim.setStartValue(QSize(10, 10))
        self.size_anim.setEndValue(QSize(100, 300))
        self.size_anim.setLoopCount(2)
        self.size_anim.finished.connect(self.delete)

        self.pos_anim = QPropertyAnimation(self.pos_btn, b'pos')
        self.pos_anim.setDuration(5000)
        self.pos_anim.setKeyValueAt(0.1, QPoint(200, 100))
        self.pos_anim.setKeyValueAt(0.5, QPoint(200, 200))
        self.pos_anim.setKeyValueAt(1.0, QPoint(200, 400))
        self.pos_anim.finished.connect(self.delete)

        self.color_anim = QPropertyAnimation(self.color_btn, b'color')
        self.color_anim.setDuration(5000)
        self.color_anim.setStartValue(QColor(0, 0, 0))
        self.color_anim.setEndValue(QColor(255, 255, 255))
        self.color_anim.finished.connect(self.delete)

    def start_anim(self):			  # 1
        if self.sender() == self.size_btn:
            self.size_anim.start()
        elif self.sender() == self.pos_btn:
            self.pos_anim.start()
        else:
            self.color_anim.start()

    def delete(self):
        if self.sender() == self.size_anim:
            self.size_btn.deleteLater()
        elif self.sender() == self.pos_anim:
            self.pos_btn.deleteLater()
        else:
            self.color_btn.deleteLater()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())