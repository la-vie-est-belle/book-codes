import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(500, 130)

        self.btn = QPushButton('开始', self)
        self.btn.resize(100, 100)
        self.btn.move(0, 0)
        self.btn.clicked.connect(self.start_anim)

        self.progress_bar = QProgressBar(self)
        self.progress_bar.setRange(0, 100)
        self.progress_bar.resize(500, 20)
        self.progress_bar.move(0, 100)

        self.time_line = QTimeLine(1000)                    # 1
        self.time_line.setFrameRange(0, 100)
        self.time_line.frameChanged.connect(self.move_btn)
        self.time_line.finished.connect(self.change_direction)
        # self.time_line.setEasingCurve(QEasingCurve.OutQuart)

    def start_anim(self):
        if self.time_line.state() == QTimeLine.NotRunning:
            self.time_line.start()

    def move_btn(self):						                # 2
        frame = self.time_line.currentFrame()
        self.btn.move(frame*4, 0)
        self.progress_bar.setValue(frame)

    def change_direction(self):					            # 3
        if self.time_line.direction() == QTimeLine.Forward:
            self.time_line.setDirection(QTimeLine.Backward)
        else:
            self.time_line.setDirection(QTimeLine.Forward)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())