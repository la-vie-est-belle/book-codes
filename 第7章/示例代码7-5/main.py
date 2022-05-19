import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QGraphicsView):
    def __init__(self):
        super(Window, self).__init__()
        self.rect1 = QGraphicsRectItem()
        self.rect2 = QGraphicsRectItem()
        self.ellipse1 = QGraphicsEllipseItem()
        self.ellipse2 = QGraphicsEllipseItem()
        self.rect1.setRect(10, 10, 100, 100)
        self.rect1.setBrush(QBrush(QColor(255, 0, 0)))
        self.rect2.setRect(150, 10, 100, 100)
        self.rect2.setBrush(QBrush(QColor(0, 0, 255)))
        self.ellipse1.setRect(10, 150, 100, 50)
        self.ellipse1.setBrush(QBrush(QColor(255, 0, 0)))
        self.ellipse2.setRect(150, 150, 100, 50)
        self.ellipse2.setBrush(QBrush(QColor(0, 0, 255)))

        self.group1 = QGraphicsItemGroup()
        self.group2 = QGraphicsItemGroup()
        self.group1.addToGroup(self.rect1)			    # 1
        self.group1.addToGroup(self.ellipse1)
        self.group1.setFlags(QGraphicsItem.ItemIsSelectable |
                               QGraphicsItem.ItemIsMovable)
        self.group2.addToGroup(self.rect2)
        self.group2.addToGroup(self.ellipse2)
        self.group2.setFlags(QGraphicsItem.ItemIsSelectable |
                               QGraphicsItem.ItemIsMovable)

        print(self.group1.boundingRect())			    # 3
        print(self.group2.boundingRect())

        self.graphics_scene = QGraphicsScene()
        self.graphics_scene.setSceneRect(0, 0, 500, 500)
        self.graphics_scene.addItem(self.group1)		# 2
        self.graphics_scene.addItem(self.group2)

        self.resize(500, 500)
        self.setScene(self.graphics_scene)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())