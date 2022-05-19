import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QGraphicsView):
    def __init__(self):
        super(Window, self).__init__()
        self.rect = QGraphicsRectItem()				# 1
        self.ellipse = QGraphicsEllipseItem()
        self.rect.setRect(100, 100, 150, 130)
        self.rect.setFlags(QGraphicsItem.ItemIsMovable |
                           QGraphicsItem.ItemIsSelectable)
        self.ellipse.setRect(100, 300, 150, 100)
        self.ellipse.setFlags(QGraphicsItem.ItemIsMovable |
                              QGraphicsItem.ItemIsSelectable)

        self.graphics_scene = QGraphicsScene()
        self.graphics_scene.setSceneRect(0, 0, 500, 500)
        self.graphics_scene.addItem(self.rect)
        self.graphics_scene.addItem(self.ellipse)

        self.resize(500, 500)
        self.setScene(self.graphics_scene)

    def mouseMoveEvent(self, event):
        super(Window, self).mouseMoveEvent(event)
        if self.ellipse.collidesWithItem(self.rect, Qt.IntersectsItemShape):    # 2
            print(self.ellipse.collidingItems(Qt.IntersectsItemShape))


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())