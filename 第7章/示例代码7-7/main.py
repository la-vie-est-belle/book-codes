import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class MyRectItem(QGraphicsObject):			            # 1
    my_signal = pyqtSignal()

    def __init__(self):
        super(MyRectItem, self).__init__()

    def boundingRect(self):				                # 2
        return QRectF(0, 0, 100, 30)

    def paint(self, painter, styles, widget=None):		# 3
        painter.drawRect(self.boundingRect())


class Window(QGraphicsView):
    def __init__(self):
        super(Window, self).__init__()
        self.rect = MyRectItem()				        # 4
        self.rect.my_signal.connect(lambda: print('signal and slot'))
        self.rect.my_signal.emit()

        self.animation = QPropertyAnimation(self.rect, b'pos')
        self.animation.setDuration(3000)
        self.animation.setStartValue(QPointF(100, 30))
        self.animation.setEndValue(QPointF(100, 200))
        self.animation.setLoopCount(-1)
        self.animation.start()

        self.graphics_scene = QGraphicsScene()
        self.graphics_scene.setSceneRect(0, 0, 500, 500)
        self.graphics_scene.addItem(self.rect)

        self.resize(500, 500)
        self.setScene(self.graphics_scene)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())