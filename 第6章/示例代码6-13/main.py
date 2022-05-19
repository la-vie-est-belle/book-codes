import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(500, 500)
        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None
        self.rect_list = []

        self.pen = QPen()
        self.pen.setWidth(2)
        self.pen.setColor(Qt.green)

        self.undo_btn = QPushButton('撤销', self)  # 5
        self.undo_btn.clicked.connect(self.undo_drawing)
        self.undo_btn.move(20, 20)

    def undo_drawing(self):
        if self.rect_list:
            self.rect_list.pop()

    def mousePressEvent(self, event):			  # 1
        if event.button() == Qt.LeftButton:
            self.x1 = event.pos().x()
            self.y1 = event.pos().y()

    def mouseMoveEvent(self, event):			  # 2
        self.x2 = event.pos().x()
        self.y2 = event.pos().y()

    def mouseReleaseEvent(self, event):			  # 3
        if self.x1 and self.y1 and self.x2 and self.y2:
            self.rect_list.append((self.x1, self.y1,
                                     self.x2-self.x1, self.y2-self.y1))

        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None

    def paintEvent(self, event):				  # 4
        painter = QPainter(self)
        painter.setPen(self.pen)

        if self.x1 and self.y1 and self.x2 and self.y2:
            painter.drawText(self.x2, self.y2, '矩形')
            painter.drawRect(self.x1, self.y1,
                              self.x2-self.x1, self.y2-self.y1)

        for rect in self.rect_list:
            painter.drawRect(rect[0], rect[1], rect[2], rect[3])

        self.update()

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())