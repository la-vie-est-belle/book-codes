from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from scene import Scene
from food import Food
from snake import Snake
from config import *
from sound import AudioSource


class GameWindow(QGraphicsView):
    def __init__(self):
        super(GameWindow, self).__init__()
        self.setWindowTitle('经典贪吃蛇')
        self.setWindowIcon(QIcon('./res/image/snake.ico'))
        qss = "QGraphicsView { border: 0px; }"
        self.setStyleSheet(qss)

        self.score = 0              # 游戏分数
        self.is_paused = False      # 游戏是否暂停
        self.is_game_over = False   # 游戏是否结束

        # 设置场景
        self.scene = Scene()
        self.setScene(self.scene)
        self.setFixedSize(self.scene.width(), self.scene.height())

        # 设置食物
        self.food = Food(self)
        self.food.spawn()

        # 设置贪吃蛇
        self.snake = Snake(self)
        self.snake.init_snake()
        self.dir_temp = self.snake.dir

        # 设置计时器
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_game)
        self.timer.start(INTERVAL)

        # 初始化音频播放对象
        self.audio_source = AudioSource()

    def update_game(self):
        self.snake.dir = self.dir_temp
        self.snake.move()

    def lose(self):
        self.is_game_over = True
        self.scene.show_lose_text()
        self.timer.stop()
        self.audio_source.play_audio('lose')

    def restart(self):
        self.is_game_over = False
        self.score = 0
        self.scene.draw_score(0)
        self.snake.init_snake()
        self.dir_temp = self.snake.dir
        self.food.spawn()
        self.scene.hide_lose_text()
        self.timer.start(INTERVAL)

    def pause(self):
        self.scene.hide_pause_button()
        self.scene.show_resume_button()
        self.is_paused = True

    def resume(self):
        self.scene.hide_resume_button()
        self.scene.show_pause_button()
        self.is_paused = False

    def keyPressEvent(self, event):
        if event.key()==Qt.Key_Up and self.snake.dir!='下':
            self.dir_temp = '上'
        elif event.key()==Qt.Key_Down and self.snake.dir!='上':
            self.dir_temp = '下'
        elif event.key()==Qt.Key_Left and self.snake.dir!='右':
            self.dir_temp = '左'
        elif event.key() == Qt.Key_Right and self.snake.dir!='左':
            self.dir_temp = '右'
        elif event.key() == Qt.Key_R and self.is_game_over:
            self.restart()
        elif event.key()==Qt.Key_Enter or event.key()==Qt.Key_Return:
            if self.is_game_over:
                return

            if not self.is_paused:
                self.pause()
            else:
                self.resume()

            self.audio_source.play_audio('pause_resume')
