import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(80, 60)

        self.sound_effect = QSoundEffect()          # 1
        self.sound_effect.setSource(QUrl.fromLocalFile('click.wav'))
        self.sound_effect.setLoopCount(1)
        self.sound_effect.setVolume(0.8)

        self.btn1 = QPushButton('播放', self)
        self.btn2 = QPushButton('关闭声音', self)
        self.btn1.move(0, 0)
        self.btn2.move(0, 30)
        self.btn1.clicked.connect(self.play)
        self.btn2.clicked.connect(self.mute_unmute)

    def play(self):
        self.sound_effect.play()

    def mute_unmute(self):			                # 2
        if self.sound_effect.isMuted():
            self.sound_effect.setMuted(False)
            self.btn2.setText('关闭声音')
        else:
            self.sound_effect.setMuted(True)
            self.btn2.setText('开启声音')


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())