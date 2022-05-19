import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.letter_group_box = QGroupBox()
        self.number_group_box = QGroupBox()

        self.letter1 = QLabel('a')
        self.letter2 = QLabel('b')
        self.letter3 = QLabel('c')
        self.number1 = QLabel('1')
        self.number2 = QLabel('2')
        self.number3 = QLabel('3')

        letter_v_layout = QVBoxLayout()
        number_v_layout = QVBoxLayout()
        window_v_layout = QVBoxLayout()
        letter_v_layout.addWidget(self.letter1)
        letter_v_layout.addWidget(self.letter2)
        letter_v_layout.addWidget(self.letter3)
        number_v_layout.addWidget(self.number1)
        number_v_layout.addWidget(self.number2)
        number_v_layout.addWidget(self.number3)
        self.letter_group_box.setLayout(letter_v_layout)
        self.number_group_box.setLayout(number_v_layout)

        self.tool_box = QToolBox()					                    # 1
        self.tool_box.addItem(self.letter_group_box, '字母')
        self.tool_box.insertItem(0, self.number_group_box, '数字')
        self.tool_box.setItemIcon(0, QIcon('number.png'))	            # 2
        self.tool_box.setItemIcon(1, QIcon('letter.png'))
        self.tool_box.currentChanged.connect(self.show_current_text)    # 3

        window_v_layout.addWidget(self.tool_box)
        self.setLayout(window_v_layout)

    def show_current_text(self):
        index = self.tool_box.currentIndex()
        print(self.tool_box.itemText(index))


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())