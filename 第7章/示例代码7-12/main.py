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
        self.rect.setRect(220, 220, 50, 50)
        self.graphics_scene.addItem(self.rect)

        self.resize(300, 300)
        self.setScene(self.graphics_scene)
        qss = "QGraphicsView { border: 0px; }"
        self.setStyleSheet(qss)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())