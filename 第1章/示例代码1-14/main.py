import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(180, 30)
        line = QLineEdit(self)
        line.textChanged.connect(self.show_text)

    def show_text(self, text):  # 1
        print(text)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())