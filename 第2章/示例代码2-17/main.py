import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.combo_box = QComboBox()
        self.combo_box.addItem('Louis')
        self.combo_box.addItems(['Mike', 'Mary', 'John'])
        self.combo_box.currentIndexChanged.connect(self.show_choice)

        self.combo_box.setEditable(True)
        self.line_edit = self.combo_box.lineEdit()                  # 1
        self.line_edit.textChanged.connect(self.show_edited_text)   # 2

        h_layout = QHBoxLayout()
        h_layout.addWidget(self.combo_box)
        self.setLayout(h_layout)

    def show_choice(self):
        print(self.combo_box.currentIndex())
        print(self.combo_box.currentText())

    def show_edited_text(self):
        print(self.line_edit.text())

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())