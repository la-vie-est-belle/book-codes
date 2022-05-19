import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.button = QToolButton()
        self.button.setToolTip('这是提示')          # 1
        self.button.setToolTipDuration(1000)

        self.button.setIcon(QIcon('button.png'))  # 2
        self.button.setIconSize(QSize(50, 50))

        self.button.setText('工具按钮')             # 3
        self.button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.button)
        self.setLayout(h_layout)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())