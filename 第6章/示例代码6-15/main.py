import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.edit = QTextEdit()
        self.print_btn = QPushButton('打印')
        self.print_btn.clicked.connect(self.print_text)

        self.printer = QPrinter()

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.edit)
        v_layout.addWidget(self.print_btn)
        self.setLayout(v_layout)

    def print_text(self):
        print_dialog = QPrintDialog(self.printer)
        if print_dialog.exec():
            self.edit.print(self.printer)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())