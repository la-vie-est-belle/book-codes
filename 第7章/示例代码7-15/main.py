import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ParentItem(QGraphicsRectItem):
    def __init__(self):
        super(ParentItem, self).__init__()
        self.setRect(100, 30, 100, 50)

    def mousePressEvent(self, event):		# 1
        print('event from parent QGraphicsItem')
        super().mousePressEvent(event)


class ChildItem(QGraphicsRectItem):
    def __init__(self):
        super(ChildItem, self).__init__()
        self.setRect(100, 30, 50, 30)

    def mousePressEvent(self, event):		# 1
        print('event from child QGraphicsItem')
        super().mousePressEvent(event)


class Scene(QGraphicsScene):
    def __init__(self):
        super(Scene, self).__init__()
        self.setSceneRect(0, 0, 300, 300)

    def mousePressEvent(self, event):		# 1
        print('event from QGraphicsScene')
        super().mousePressEvent(event)


class Window(QGraphicsView):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(300, 300)

        self.scene = Scene()
        self.setScene(self.scene)

        self.parent_item = ParentItem()
        self.child_item = ChildItem()
        self.child_item.setParentItem(self.parent_item)
        self.scene.addItem(self.parent_item)

    def mousePressEvent(self, event):		# 1
        print('event from QGraphicsView')
        super().mousePressEvent(event)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())