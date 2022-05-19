import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QGraphicsView):
    def __init__(self):
        super(Window, self).__init__()
        self.graphics_scene = QGraphicsScene()
        self.graphics_scene.setSceneRect(0, 0, 300, 300)

        self.rect = QGraphicsRectItem()
        self.rect.setRect(50, 50, 50, 50)
        self.rect.setBrush(QBrush(QColor(255, 0, 0)))
        self.ellipse = QGraphicsEllipseItem()
        self.ellipse.setRect(100, 100, 50, 50)
        self.ellipse.setBrush(QBrush(QColor(0, 255, 0)))

        self.graphics_scene.addItem(self.rect)
        self.graphics_scene.addItem(self.ellipse)

        self.move(10, 10)
        self.resize(300, 300)
        self.setScene(self.graphics_scene)

    def mousePressEvent(self, event):		# 1
        self.rotate(10)

    def wheelEvent(self, event):			# 2
        if event.angleDelta().y() < 0:
            self.scale(0.9, 0.9)
        else:
            self.scale(1.1, 1.1)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())