import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.label = QLabel('0')
        self.label.setAlignment(Qt.AlignCenter)
        self.btn = QPushButton('计数')
        self.btn.clicked.connect(self.count)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.label)
        v_layout.addWidget(self.btn)
        self.setLayout(v_layout)

        self.count_thread = CountThread()       # 2
        self.count_thread.count_signal.connect(self.update_label)

    def count(self):
        self.count_thread.start()

    def update_label(self, num):
        self.label.setText(str(num))


class CountThread(QThread):                     # 1
    count_signal = pyqtSignal(int)

    def __init__(self):
        super(CountThread, self).__init__()

    def run(self):
        num = 0
        while num < 10000000:
            num += 1
            self.count_signal.emit(num)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())