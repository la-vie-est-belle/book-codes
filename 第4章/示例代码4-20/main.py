import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(300, 300)
        self.status_bar = QStatusBar()
        self.progress_bar = QProgressBar()
        self.status_bar.addWidget(self.progress_bar)    # 1
        self.setStatusBar(self.status_bar)

        self.btn = QPushButton('计数', self)
        self.btn.clicked.connect(self.count)

        self.value = 0                                  # 2
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress_bar)

    def count(self):
        self.value = 0
        self.timer.start(50)
        self.progress_bar.setValue(0)
        self.status_bar.clearMessage()

    def update_progress_bar(self):
        self.value += 1
        self.progress_bar.setValue(self.value)

        if self.value == 100:
            self.timer.stop()
            self.status_bar.showMessage('结束')


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())