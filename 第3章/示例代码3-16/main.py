import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.text_edit = QTextEdit()
        self.btn = QPushButton('显示颜色对话框')
        self.btn.clicked.connect(self.set_color)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.text_edit)
        v_layout.addWidget(self.btn)
        self.setLayout(v_layout)

    def set_color(self):			# 1
        color = QColorDialog.getColor()
        if color.isValid():
            print(color.name())
            print(color.red(), color.green(), color.blue())
            self.text_edit.setTextColor(color)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())