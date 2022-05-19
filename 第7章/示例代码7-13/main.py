import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QGraphicsView):
    def __init__(self):
        super(Window, self).__init__()
        self.graphics_scene = QGraphicsScene()
        self.graphics_scene.setSceneRect(0, 0, 100, 100)

        self.rect1 = QGraphicsRectItem()
        self.rect1.setRect(0, 0, 50, 50)
        self.rect1.setBrush(QBrush(QColor(255, 0, 0)))
        self.rect2 = QGraphicsRectItem()
        self.rect2.setRect(0, 50, 50, 50)
        self.rect2.setBrush(QBrush(QColor(0, 255, 0)))
        self.rect3 = QGraphicsRectItem()
        self.rect3.setRect(50, 0, 50, 50)
        self.rect3.setBrush(QBrush(QColor(0, 0, 255)))
        self.rect4 = QGraphicsRectItem()
        self.rect4.setRect(50, 50, 50, 50)
        self.rect4.setBrush(QBrush(QColor(255, 0, 255)))

        self.graphics_scene.addItem(self.rect1)
        self.graphics_scene.addItem(self.rect2)
        self.graphics_scene.addItem(self.rect3)
        self.graphics_scene.addItem(self.rect4)

        self.resize(200, 200)
        self.setScene(self.graphics_scene)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())