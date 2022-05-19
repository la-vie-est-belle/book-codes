import random
from PyQt5.QtWidgets import *
from config import *
from sound import AudioSource


class Snake:
    def __init__(self, game):
        super(Snake, self).__init__()
        self.game = game                # 游戏主窗口
        self.scene = self.game.scene    # 游戏场景
        self.dir = None                 # 移动方向
        self.pos_list = []              # 身体坐标
        self.snake_items_list = []      # 组成蛇的各个项

    def init_snake(self):
        """初始化贪吃蛇"""
        self.pos_list = []

        # 确定蛇头
        x, y = self.get_random_pos()
        self.pos_list.append([x, y])

        # 随机确定蛇身和移动方向
        while True:
            num = random.randint(1, 4)
            if num == 1 and x-2 >= AREA_START_X:    # 蛇身朝左，向右移动
                self.pos_list.append([x-1, y])
                self.pos_list.append([x-2, y])
                self.dir = '右'
                break
            elif num == 2 and x+2 <= AREA_END_X:    # 蛇身朝右，向左移动
                self.pos_list.append([x+1, y])
                self.pos_list.append([x+2, y])
                self.dir = '左'
                break
            elif num == 3 and y-2 >= AREA_START_Y:  # 蛇身朝上，向下移动
                self.pos_list.append([x, y-1])
                self.pos_list.append([x, y-2])
                self.dir = '下'
                break
            elif num == 4 and y+2 <= AREA_END_Y:    # 蛇身朝下，向上移动
                self.pos_list.append([x, y+1])
                self.pos_list.append([x, y+2])
                self.dir = '上'
                break

        self.draw_snake(self.pos_list)

    def get_random_pos(self):
        x = random.randint(AREA_START_X, AREA_END_X)
        y = random.randint(AREA_START_Y, AREA_END_Y)
        return x, y

    def draw_snake(self, pos_list):
        self.clear()

        for pos in pos_list:
            x = pos[0]
            y = pos[1]
            block = self.draw_block(x*BLOCK_WIDTH, y*BLOCK_WIDTH)
            self.snake_items_list.append(block[0])
            self.snake_items_list.append(block[1])

    def clear(self):
        for item in self.snake_items_list:
            self.scene.removeItem(item)

        self.snake_items_list = []

    def draw_block(self, x, y):
        rect_item1 = QGraphicsRectItem()
        rect_item2 = QGraphicsRectItem()
        rect_item1.setRect(x, y, BLOCK_WIDTH, BLOCK_WIDTH)
        rect_item2.setRect(x+2, y+2, BLOCK_WIDTH-4, BLOCK_WIDTH-4)

        rect_item1.setBrush(BLOCK_COLOR)
        rect_item2.setBrush(BLOCK_COLOR)
        rect_item1.setOpacity(0.5)
        rect_item2.setOpacity(0.5)
        self.scene.addItem(rect_item1)
        self.scene.addItem(rect_item2)

        return (rect_item1, rect_item2)

    def move(self):
        head_pos = list(self.pos_list[0])
        if self.dir == '左':
            head_pos[0] -= 1
        elif self.dir == '右':
            head_pos[0] += 1
        elif self.dir == '上':
            head_pos[1] -= 1
        elif self.dir == '下':
            head_pos[1] += 1

        # 检查是有有碰撞
        self.check_collision(head_pos)

        # 如果游戏暂停或失败，则停止蛇的移动
        if not self.game.is_paused and not self.game.is_game_over:
            self.pos_list.insert(0, head_pos)

            # 检查是否有吃到食物
            if head_pos != self.game.food.food_pos:
                self.pos_list.pop()
            else:
                self.game.score += 1
                self.scene.draw_score(self.game.score)
                self.game.food.spawn()
                self.game.audio_source.play_audio('eat')

            self.draw_snake(self.pos_list)

    def check_collision(self, head_pos):
        # 检查是否有碰撞
        for i, pos in enumerate(self.pos_list):
            if i!=0 and head_pos==pos:
                self.game.lose()
                return

        # 检查蛇头是否超出移动范围
        if head_pos[0] < AREA_START_X or head_pos[0] > AREA_END_X or \
           head_pos[1] < AREA_START_Y or head_pos[1] > AREA_END_Y:
            self.game.lose()
