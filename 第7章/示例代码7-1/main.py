import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QGraphicsView):
    def __init__(self):
        super(Window, self).__init__()
        self.ellipse = QGraphicsEllipseItem()
        self.ellipse.setRect(0, 100, 50, 100)

        self.line = QGraphicsLineItem()
        self.line.setLine(100, 100, 100, 200)

        self.path = QGraphicsPathItem()
        tri_path = QPainterPath()
        tri_path.moveTo(150, 100)
        tri_path.lineTo(200, 100)
        tri_path.lineTo(200, 200)
        tri_path.lineTo(150, 100)
        tri_path.closeSubpath()
        self.path.setPath(tri_path)

        self.pixmap = QGraphicsPixmapItem()			    # 1
        self.pixmap.setPixmap(QPixmap('qt.png').scaled(100, 100))
        self.pixmap.setPos(250, 100)
        self.pixmap.setFlags(QGraphicsItem.ItemIsMovable)

        self.polygon = QGraphicsPolygonItem()
        point1 = QPointF(400.0, 100.0)
        point2 = QPointF(420.0, 150.0)
        point3 = QPointF(430.0, 200.0)
        point4 = QPointF(380.0, 110.0)
        point5 = QPointF(350.0, 110.0)
        point6 = QPointF(400.0, 100.0)
        self.polygon.setPolygon(QPolygonF([point1, point2, point3,
                                              point4, point5, point6]))

        self.rect = QGraphicsRectItem()
        self.rect.setRect(450, 100, 50, 100)

        self.simple_text = QGraphicsSimpleTextItem()
        self.simple_text.setText('Hello PyQt!')
        self.simple_text.setPos(550, 100)

        self.rich_text = QGraphicsTextItem()
        self.rich_text.setHtml('<p style="font-size:10px">Hello PyQt!</p>')
        self.rich_text.setPos(650, 100)
        self.rich_text.setTextInteractionFlags(Qt.TextEditorInteraction) # 2
        self.rich_text.setDefaultTextColor(QColor(100, 100, 100))	     # 3

        self.graphics_scene = QGraphicsScene()			# 4
        self.graphics_scene.setSceneRect(0, 0, 750, 300)
        self.graphics_scene.addItem(self.ellipse)
        self.graphics_scene.addItem(self.line)
        self.graphics_scene.addItem(self.path)
        self.graphics_scene.addItem(self.pixmap)
        self.graphics_scene.addItem(self.polygon)
        self.graphics_scene.addItem(self.rect)
        self.graphics_scene.addItem(self.simple_text)
        self.graphics_scene.addItem(self.rich_text)

        self.resize(750, 300)					        # 5
        self.setScene(self.graphics_scene)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())