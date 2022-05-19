import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.Qt import QVideoWidget


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(600, 400)

        video1 = QUrl.fromLocalFile('./video1.mp4')
        video2 = QUrl.fromLocalFile('./video2.mp4')
        video3 = QUrl.fromLocalFile('./video3.mp4')

        self.playlist = QMediaPlaylist()                # 1
        self.playlist.addMedia(QMediaContent(video1))
        self.playlist.addMedia(QMediaContent(video2))
        self.playlist.addMedia(QMediaContent(video3))
        self.playlist.setCurrentIndex(0)
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)
        self.playlist.currentMediaChanged.connect(self.show_info)

        self.video_widget = QVideoWidget()

        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)
        self.player.setVideoOutput(self.video_widget)

        self.btn1 = QPushButton('上一个', self)
        self.btn2 = QPushButton('播放/停止', self)
        self.btn3 = QPushButton('下一个', self)
        self.btn1.clicked.connect(self.control)
        self.btn2.clicked.connect(self.control)
        self.btn3.clicked.connect(self.control)

        btn_h_layout = QHBoxLayout()
        window_v_layout = QVBoxLayout()
        btn_h_layout.addWidget(self.btn1)
        btn_h_layout.addWidget(self.btn2)
        btn_h_layout.addWidget(self.btn3)
        window_v_layout.addWidget(self.video_widget)
        window_v_layout.addLayout(btn_h_layout)
        self.setLayout(window_v_layout)

    def show_info(self):
        print('索引：', self.playlist.currentIndex())
        print('当前媒体：', self.playlist.currentMedia())

    def control(self):
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