import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QGraphicsView):
    def __init__(self):
        super(Window, self).__init__()
        self.graphics_scene = QGraphicsScene()
        self.graphics_scene.setSceneRect(0, 0, 300, 300)
        self.graphics_scene.focusItemChanged.connect(self.show_item)    # 2

        self.ellipse = self.graphics_scene.addEllipse(50, 100, 50, 100) # 1
        self.ellipse.setFlags(QGraphicsItem.ItemIsFocusable)
        self.rect = self.graphics_scene.addRect(150, 100, 100, 100)
        self.rect.setFlags(QGraphicsItem.ItemIsFocusable)

        print(self.graphics_scene.items())                      # 3
        print(self.graphics_scene.itemsBoundingRect())          # 4

        self.resize(300, 300)
        self.setScene(self.graphics_scene)

    def show_item(self, new_item, old_item):
        print(f'new item: {new_item}')
        print(f'old item: {old_item}')

    def mousePressEvent(self, event):                           # 5
        super(Window, self).mousePressEvent(event)
        pos = event.pos()
        item = self.graphics_scene.itemAt(pos, QTransform())
        print(item)

    def mouseDoubleClickEvent(self, event):                     # 6
        super(Window, self).mouseDoubleClickEvent(event)
        pos = event.pos()
        item = self.graphics_scene.itemAt(pos, QTransform())
        if item:
            self.graphics_scene.removeItem(item)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())