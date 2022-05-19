import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()

        self.btn = QPushButton('QPushButton')
        self.label = QLabel('QLabel')
        self.line_edit = QLineEdit()
        self.text_edit = QTextEdit()
        self.line_edit.setText('QLineEdit')
        self.text_edit.setText('QTextEdit')

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.btn)
        v_layout.addWidget(self.label)
        v_layout.addWidget(self.line_edit)
        v_layout.addWidget(self.text_edit)
        self.setLayout(v_layout)


if __name__ == '__main__':
    with open('style.qss', 'r', encoding='utf-8') as f:
        qss = f.read()

    app = QApplication([])
    app.setStyleSheet(qss)

    window = Window()
    window.show()
    sys.exit(app.exec())