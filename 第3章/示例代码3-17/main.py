import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.text_edit = QTextEdit()
        self.btn = QPushButton('显示字体对话框')
        self.btn.clicked.connect(self.set_font)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.text_edit)
        v_layout.addWidget(self.btn)
        self.setLayout(v_layout)

    def set_font(self):		           # 1
        font, isOk = QFontDialog.getFont()
        if isOk:
            print(font.family())
            print(font.pointSize())
            self.text_edit.setFont(font)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())