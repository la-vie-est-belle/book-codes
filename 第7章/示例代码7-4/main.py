import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QGraphicsView):
    def __init__(self):
        super(Window, self).__init__()
        self.rect1 = QGraphicsRectItem()
        self.rect1.setRect(0, 0, 200, 200)
        self.rect1.setBrush(QBrush(QColor(255, 0, 0)))
        self.rect1.moveBy(100, 100)			            # 1
        self.rect1.setScale(1.5)				        # 2
        self.rect1.setRotation(45)				        # 3
        self.rect1.setTransformOriginPoint(100, 100)	# 4

        self.graphics_scene = QGraphicsScene()
        self.graphics_scene.setSceneRect(0, 0, 500, 500)
        self.graphics_scene.addItem(self.rect1)

        self.resize(500, 500)
        self.setScene(self.graphics_scene)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())