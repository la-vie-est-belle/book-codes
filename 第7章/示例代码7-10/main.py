import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QGraphicsView):
    def __init__(self):
        super(Window, self).__init__()
        self.graphics_scene = QGraphicsScene()
        self.graphics_scene.setSceneRect(0, 0, 260, 80)

        self.user_label = QLabel('Username:')
        self.pass_label = QLabel('Password:')
        self.user_line = QLineEdit()
        self.pass_line = QLineEdit()
        self.user_label.setAttribute(Qt.WA_TranslucentBackground)
        self.pass_label.setAttribute(Qt.WA_TranslucentBackground)
        self.user_line.setAttribute(Qt.WA_TranslucentBackground)
        self.pass_line.setAttribute(Qt.WA_TranslucentBackground)

        self.user_label_proxy = self.graphics_scene.addWidget(self.user_label)
        self.pass_label_proxy = self.graphics_scene.addWidget(self.pass_label)
        self.user_line_proxy = self.graphics_scene.addWidget(self.user_line)
        self.pass_line_proxy = self.graphics_scene.addWidget(self.pass_line)

        linear_layout1 = QGraphicsLinearLayout()		# 1
        linear_layout2 = QGraphicsLinearLayout()
        linear_layout3 = QGraphicsLinearLayout()
        linear_layout3.setOrientation(Qt.Vertical)
        linear_layout1.addItem(self.user_label_proxy)
        linear_layout1.addItem(self.user_line_proxy)
        linear_layout2.addItem(self.pass_label_proxy)
        linear_layout2.addItem(self.pass_line_proxy)
        linear_layout3.addItem(linear_layout1)
        linear_layout3.addItem(linear_layout2)

        graphics_widget = QGraphicsWidget()
        graphics_widget.setLayout(linear_layout3)		# 2
        self.graphics_scene.addItem(graphics_widget)

        self.resize(260, 80)
        self.setScene(self.graphics_scene)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())