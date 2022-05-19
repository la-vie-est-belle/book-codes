import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(100, 30)

        self.sound = QSound('audio.wav')    # 1
        self.sound.setLoops(2)

        self.btn = QPushButton('播放/停止', self)
        self.btn.clicked.connect(self.play_or_stop)

    def play_or_stop(self):		            # 2
        if self.sound.isFinished():
            self.sound.play()
        else:
            self.sound.stop()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())