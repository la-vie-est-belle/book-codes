import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QGraphicsView):
    def __init__(self):
        super(Window, self).__init__()
        self.graphics_scene = QGraphicsScene()
        self.graphics_scene.setSceneRect(0, 0, 220, 100)

        self.label = QLabel('label')
        self.button = QPushButton('button')

        self.label_proxy = self.graphics_scene.addWidget(self.label)    # 1
        self.button_proxy = self.graphics_scene.addWidget(self.button)
        self.label.setAttribute(Qt.WA_TranslucentBackground)
        self.button.setAttribute(Qt.WA_TranslucentBackground)
        self.label_proxy.setPos(10, 20)
        self.button_proxy.setPos(50, 20)

        self.resize(220, 100)
        self.setScene(self.graphics_scene)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())