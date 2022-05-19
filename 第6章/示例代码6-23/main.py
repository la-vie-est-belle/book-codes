import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(260, 30)

        audio1 = QUrl.fromLocalFile('./audio1.wav')     # 1
        audio2 = QUrl.fromLocalFile('./audio2.mp3')
        audio3 = QUrl.fromLocalFile('./audio3.mp3')

        self.playlist = QMediaPlaylist()
        self.playlist.addMedia(QMediaContent(audio1))
        self.playlist.addMedia(QMediaContent(audio2))
        self.playlist.addMedia(QMediaContent(audio3))
        self.playlist.setCurrentIndex(0)
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.playlist.currentMediaChanged.connect(self.show_info)

        self.player = QMediaPlayer()                    # 2
        self.player.setPlaylist(self.playlist)
        self.player.setVolume(90)

        self.btn1 = QPushButton('上一首', self)
        self.btn2 = QPushButton('播放/停止', self)
        self.btn3 = QPushButton('下一首', self)
        self.btn1.move(0, 0)
        self.btn2.move(90, 0)
        self.btn3.move(190, 0)
        self.btn1.clicked.connect(self.control)
        self.btn2.clicked.connect(self.control)
        self.btn3.clicked.connect(self.control)

    def show_info(self):                                # 3
        print('当前媒体：', self.playlist.currentMedia())
        print('索引：', self.playlist.currentIndex())

    def control(self):                                  # 4
        print('媒体状态：', self.player.mediaStatus())

        if self.sender() == self.btn1:
            self.playlist.previous()
        elif self.sender() == self.btn2:
            if self.player.state() == QMediaPlayer.StoppedState:
                self.player.play()
            else:
                self.player.stop()
        else:
            self.playlist.next()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())