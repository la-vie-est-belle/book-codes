import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class ColorButton(QPushButton):
    def __init__(self, text=None, parent=None):
        super(ColorButton, self).__init__(text, parent)
        self._color = QColor()

    @pyqtProperty(QColor)		# 1
    def color(self):
        return self._color

    @color.setter			    # 2
    def color(self, value):
        self._color = value
        red = value.red()
        green = value.green()
        blue = value.blue()
        self.setStyleSheet(f'background-color: rgb({red}, {green}, {blue})')

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.color_btn = ColorButton('颜色', self)
        self.color_btn.move(20, 20)
        self.color_btn.resize(100, 100)
        self.color_btn.clicked.connect(self.start_anim)

        self.color_anim = QPropertyAnimation(self.color_btn, b'color')
        self.color_anim.setDuration(5000)
        self.color_anim.setStartValue(QColor(0, 0, 0))
        self.color_anim.setEndValue(QColor(255, 255, 255))
        self.color_anim.finished.connect(self.delete)

    def start_anim(self):
        self.color_anim.start()

    def delete(self):
        self.color_btn.deleteLater()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())