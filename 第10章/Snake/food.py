from PyQt5.QtWidgets import *
from config import *
import random


class Food:
    def __init__(self, game):
        super(Food, self).__init__()
        self.game = game                # 游戏主窗口
        self.scene = self.game.scene    # 游戏场景

        self.food_pos = []              # 食物当前坐标
        self.food_items_list = []       # 组成食物方块的矩形图元

    def spawn(self):
        """生成食物"""
        self.clear()
        x, y = self.get_random_pos()
        block = self.draw_block(x*BLOCK_WIDTH, y*BLOCK_WIDTH)
        self.food_items_list.append(block[0])
        self.food_items_list.append(block[1])

    def clear(self):
        """清空食物"""
        for item in self.food_items_list:
            self.scene.removeItem(item)

        self.food_items_list = []

    def get_random_pos(self):
        """获取随机位置"""
        # while True:
        #     x = random.randint(AREA_START_X, AREA_END_X)
        #     y = random.randint(AREA_START_Y, AREA_END_Y)
        #     self.food_pos = [x, y]
        #
        #     # # 食物不能和贪吃蛇的任何方块重合
        #     # if self.food_pos not in self.game.snake.pos_list:
        #     #     return x, y
        x = random.randint(AREA_START_X, AREA_END_X)
        y = random.randint(AREA_START_Y, AREA_END_Y)
        self.food_pos = [x, y]
        return x, y

    def draw_block(self, x, y):
        rect_item1 = QGraphicsRectItem()
        rect_item2 = QGraphicsRectItem()
        rect_item1.setRect(x, y, BLOCK_WIDTH, BLOCK_WIDTH)
        rect_item2.setRect(x+2, y+2, BLOCK_WIDTH-4, BLOCK_WIDTH-4)

        rect_item1.setBrush(FOOD_COLOR)
        rect_item2.setBrush(FOOD_COLOR)
        rect_item1.setOpacity(0.5)
        rect_item2.setOpacity(0.5)
        self.scene.addItem(rect_item1)
        self.scene.addItem(rect_item2)

        return (rect_item1, rect_item2)