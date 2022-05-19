import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QGraphicsView):
    def __init__(self):
        super(Window, self).__init__()
        self.graphics_scene = QGraphicsScene()
        self.graphics_scene.setSceneRect(0, 0, 300, 300)

        self.ellipse = self.graphics_scene.addEllipse(50, 100, 50, 100)
        self.rect = self.graphics_scene.addRect(150, 100, 100, 100)

        self.resize(500, 500)
        self.setScene(self.graphics_scene)

    def mousePressEvent(self, event):
        super(Window, self).mousePressEvent(event)
        pos = self.mapToScene(event.pos())
        item = self.graphics_scene.itemAt(pos, QTransform())    # 1
        print(item)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())