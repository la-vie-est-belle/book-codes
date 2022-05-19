import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.label = QLabel('0')
        self.label.setAlignment(Qt.AlignCenter)
        self.btn1 = QPushButton('计数')
        self.btn2 = QPushButton('停止')
        self.btn1.clicked.connect(self.start_counting)
        self.btn2.clicked.connect(self.stop_counting)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.label)
        v_layout.addWidget(self.btn1)
        v_layout.addWidget(self.btn2)
        self.setLayout(v_layout)

        self.count_thread = CountThread()
        self.count_thread.count_signal.connect(self.update_label)

    def start_counting(self):                   # 1
        if not self.count_thread.isRunning():
            self.count_thread.start()

    def stop_counting(self):
        self.count_thread.stop()

    def update_label(self, num):
        self.label.setText(str(num))


class CountThread(QThread):
    count_signal = pyqtSignal(int)

    def __init__(self):
        super(CountThread, self).__init__()
        self.flag = True

    def run(self):
        num = 0
        self.flag = True

        while num < 10000000:
            if not self.flag:
                break

            num += 1
            self.count_signal.emit(num)
            self.msleep(100)			        # 3

    def stop(self):				                # 2
        self.flag = False


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())