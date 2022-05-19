import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *


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

        self.undo_btn = QPushButton('撤销', self)
        self.undo_btn.clicked.connect(self.undo_drawing)
        self.undo_btn.move(20, 20)

        self.printer = QPrinter()           # 1

        self.print_btn = QPushButton('打印', self)
        self.print_btn.clicked.connect(self.print_drawing)
        self.print_btn.move(20, 50)

    def undo_drawing(self):
        if self.rect_list:
            self.rect_list.pop()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.x1 = event.pos().x()
            self.y1 = event.pos().y()

    def mouseMoveEvent(self, event):
        self.x2 = event.pos().x()
        self.y2 = event.pos().y()

    def mouseReleaseEvent(self, event):
        if self.x1 and self.y1 and self.x2 and self.y2:
            self.rect_list.append((self.x1, self.y1,
                                     self.x2-self.x1, self.y2-self.y1))

        self.x1 = None
        self.y1 = None
        self.x2 = None
        self.y2 = None

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(self.pen)

        if self.x1 and self.y1 and self.x2 and self.y2:
            painter.drawText(self.x2, self.y2, '矩形')
            painter.drawRect(self.x1, self.y1,
                              self.x2-self.x1, self.y2-self.y1)

        for rect in self.rect_list:
            painter.drawRect(rect[0], rect[1], rect[2], rect[3])

        self.update()

    def print_drawing(self):                # 2
        print_dialog = QPrintDialog(self.printer)
        if print_dialog.exec():
            painter = QPainter(self.printer)
            painter.setPen(self.pen)
            for rect in self.rect_list:
                painter.drawRect(rect[0], rect[1], rect[2], rect[3])


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())