import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(500, 500)

        self.start_btn = QPushButton('开始', self)
        self.stop_btn = QPushButton('停止', self)
        self.pause_resume_btn = QPushButton('暂停/继续', self)
        self.start_btn.move(20, 20)
        self.stop_btn.move(20, 50)
        self.pause_resume_btn.move(20, 80)
        self.start_btn.clicked.connect(self.control_anim)
        self.stop_btn.clicked.connect(self.control_anim)
        self.pause_resume_btn.clicked.connect(self.control_anim)

        self.plane = QLabel(self)
        self.plane.move(200, 400)
        self.plane.setPixmap(QPixmap('plane.png'))
        self.plane.setScaledContents(True)

        self.anim1 = QPropertyAnimation(self.plane, b'pos')     # 1
        self.anim1.setDuration(2000)
        self.anim1.setStartValue(QPoint(200, 400))
        self.anim1.setEndValue(QPoint(200, 300))
        self.anim2 = QPropertyAnimation(self.plane, b'pos')
        self.anim2.setDuration(3000)
        self.anim2.setStartValue(QPoint(200, 300))
        self.anim2.setEndValue(QPoint(100, 200))

        self.anim_group = QSequentialAnimationGroup()           # 2
        self.anim_group.addAnimation(self.anim1)
        self.anim_group.addPause(1000)
        self.anim_group.addAnimation(self.anim2)
        self.anim_group.stateChanged.connect(self.get_info)
        print(self.anim_group.totalDuration())

    def get_info(self):					                        # 3
        print(self.anim_group.currentAnimation())
        print(self.anim_group.currentTime())

    def control_anim(self):				                        # 4
        if self.sender() == self.start_btn:
            self.anim_group.start()
        elif self.sender() == self.stop_btn:
            self.anim_group.stop()
        else:
            if self.anim_group.state() == QAbstractAnimation.Paused:
                self.anim_group.resume()
            else:
                self.anim_group.pause()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())