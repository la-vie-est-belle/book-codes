import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.btn1 = QPushButton('button1', self)
        self.btn2 = QPushButton('button2', self)
        self.btn2.setProperty('name', 'btn')                # 1
        print(self.btn2.property('name'))

        self.line_edit1 = QLineEdit(self)
        self.line_edit1.setPlaceholderText('line edit')
        self.line_edit2 = SubLineEdit()

        self.combo_box = QComboBox(self)                    # 2
        self.combo_box.addItems(['A', 'B', 'C', 'D'])
        self.combo_box.setObjectName('cb')

        self.group_box = QGroupBox()                        # 3
        self.label1 = QLabel('label1')
        self.label2 = QLabel('label2')
        self.stack = QStackedWidget()
        self.stack.addWidget(self.label2)

        gb_layout = QVBoxLayout()
        v_layout = QVBoxLayout()
        gb_layout.addWidget(self.label1)
        gb_layout.addWidget(self.stack)
        self.group_box.setLayout(gb_layout)
        v_layout.addWidget(self.btn1)
        v_layout.addWidget(self.btn2)
        v_layout.addWidget(self.line_edit1)
        v_layout.addWidget(self.line_edit2)
        v_layout.addWidget(self.combo_box)
        v_layout.addWidget(self.group_box)
        self.setLayout(v_layout)


class SubLineEdit(QLineEdit):
    def __init__(self):
        super(SubLineEdit, self).__init__()
        self.setPlaceholderText('sub line edit')


if __name__ == '__main__':
    with open('style.qss', 'r', encoding='utf-8') as f:
        qss = f.read()

    app = QApplication([])
    app.setStyleSheet(qss)

    window = Window()
    window.show()
    sys.exit(app.exec())