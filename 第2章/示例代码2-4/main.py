import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.movie = QMovie()			    # 1
        self.movie.setFileName('./flash.gif')
        self.movie.jumpToFrame(0)

        self.label = QLabel()
        self.label.setMovie(self.movie)		# 2
        self.label.setAlignment(Qt.AlignCenter)

        self.start_btn = QPushButton('开始')
        self.pause_resume_btn = QPushButton('暂停')
        self.stop_btn = QPushButton('停止')
        self.speed_up_btn = QPushButton('加速')
        self.speed_down_btn = QPushButton('减速')
        self.start_btn.clicked.connect(self.control)
        self.pause_resume_btn.clicked.connect(self.control)
        self.stop_btn.clicked.connect(self.control)
        self.speed_up_btn.clicked.connect(self.control)
        self.speed_down_btn.clicked.connect(self.control)

        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        h_layout.addWidget(self.start_btn)
        h_layout.addWidget(self.pause_resume_btn)
        h_layout.addWidget(self.stop_btn)
        h_layout.addWidget(self.speed_up_btn)
        h_layout.addWidget(self.speed_down_btn)
        v_layout.addWidget(self.label)
        v_layout.addLayout(h_layout)
        self.setLayout(v_layout)

    def control(self):				        # 3
        if self.sender() == self.start_btn:
            self.movie.start()
        elif self.sender() == self.pause_resume_btn:
            if self.pause_resume_btn.text() == '暂停':
                self.movie.setPaused(True)
                self.pause_resume_btn.setText('继续')
            else:
                self.movie.setPaused(False)
                self.pause_resume_btn.setText('暂停')
        elif self.sender() == self.stop_btn:
            self.movie.stop()
            self.movie.jumpToFrame(0)
        elif self.sender() == self.speed_up_btn:
            speed = self.movie.speed()
            self.movie.setSpeed(speed*2)
        elif self.sender() == self.speed_down_btn:
            speed = self.movie.speed()
            self.movie.setSpeed(speed/2)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())