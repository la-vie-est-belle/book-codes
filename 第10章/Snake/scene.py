from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from pathlib import Path
from config import *


class Scene(QGraphicsScene):
    def __init__(self):
        super(Scene, self).__init__()
        self.setSceneRect(0, 0, SCENE_WIDTH, SCENE_HEIGHT)

        self.score_item = None
        self.pause_btn_items_list = []
        self.resume_btn_items_list = []
        self.lose_text_item = None

        self.draw_scene()

    def draw_scene(self):
        """绘制场景上的各项内容"""
        self.draw_bg()                  # 绘制背景
        self.draw_logo()                # 绘制图标
        self.draw_score(0)              # 绘制分数
        self.draw_move_area()           # 绘制可移动区域
        self.draw_move_area_frame()     # 绘制区域边框
        self.draw_pause_button()        # 绘制暂停按钮
        self.draw_resume_button()       # 绘制继续按钮
        self.draw_lose_text()           # 绘制游戏失败提示

    def draw_bg(self):
        self.setBackgroundBrush(BG_COLOR)

    def draw_logo(self):
        log_path = str(Path(__file__).parent / 'res/image/snake.ico')
        pixmap_item = QGraphicsPixmapItem()
        pixmap_item.setPixmap(QPixmap(log_path))
        pixmap_item.setOpacity(0.2)

        x = SCENE_WIDTH/2 - pixmap_item.boundingRect().width()/2
        y = BLOCK_WIDTH/2
        pixmap_item.setPos(x, y)
        self.addItem(pixmap_item)

    def draw_score(self, value):
        if not self.score_item:
            score_item = QGraphicsSimpleTextItem()
            score_item.setText("分数："+str(value))
            score_item.setScale(2.3)
            score_item.setOpacity(0.3)
            score_item.setPos(BLOCK_WIDTH, BLOCK_WIDTH)
            self.score_item = score_item
            self.addItem(self.score_item)
        else:
            self.score_item.setText("分数："+str(value))

    def draw_block(self, x, y):
        rect_item1 = QGraphicsRectItem()
        rect_item2 = QGraphicsRectItem()
        rect_item1.setRect(x, y, BLOCK_WIDTH, BLOCK_WIDTH)
        rect_item2.setRect(x+2, y+2, BLOCK_WIDTH-4, BLOCK_WIDTH-4)

        rect_item1.setBrush(BLOCK_COLOR)
        rect_item2.setBrush(BLOCK_COLOR)
        rect_item1.setOpacity(0.04)
        rect_item2.setOpacity(0.04)
        self.addItem(rect_item1)
        self.addItem(rect_item2)

        return (rect_item1, rect_item2)

    def draw_move_area(self):
        """绘制贪吃蛇可移动的区域"""
        for x in range(HORIZONTAL_BLOCK_NUM):
            for y in range(VERTICAL_BLOCK_NUM):
                if AREA_START_X <= x <= AREA_END_X and AREA_START_Y <= y <= AREA_END_Y:
                    self.draw_block(x*BLOCK_WIDTH, y*BLOCK_WIDTH)

    def draw_move_area_frame(self):
        """绘制区域边框"""
        rect_item = QGraphicsRectItem()

        offset = 3
        x = AREA_START_X * BLOCK_WIDTH - offset
        y = AREA_START_Y * BLOCK_WIDTH - offset
        width = AREA_END_X * BLOCK_WIDTH + offset * 2
        height = (AREA_END_Y-AREA_START_Y+1) * BLOCK_WIDTH + offset * 2
        rect_item.setRect(x, y, width, height)
        self.addItem(rect_item)

    def draw_pause_button(self):
        """绘制暂停按钮"""
        for i in range(3):
            x = (HORIZONTAL_BLOCK_NUM-4) * BLOCK_WIDTH
            y = (i+1) * BLOCK_WIDTH
            block = self.draw_block(x, y)
            self.pause_btn_items_list.append(block[0])
            self.pause_btn_items_list.append(block[1])

        for i in range(3):
            x = (HORIZONTAL_BLOCK_NUM-2) * BLOCK_WIDTH
            y = (i+1) * BLOCK_WIDTH
            block = self.draw_block(x, y)
            self.pause_btn_items_list.append(block[0])
            self.pause_btn_items_list.append(block[1])

    def draw_resume_button(self):
        """绘制继续按钮"""
        for i in range(3):
            x = (HORIZONTAL_BLOCK_NUM-4) * BLOCK_WIDTH
            y = (i+1) * BLOCK_WIDTH
            block = self.draw_block(x, y)
            self.resume_btn_items_list.append(block[0])
            self.resume_btn_items_list.append(block[1])

        for i in range(2):
            x = (HORIZONTAL_BLOCK_NUM-3) * BLOCK_WIDTH
            y = (i+1.5) * BLOCK_WIDTH
            block = self.draw_block(x, y)
            self.resume_btn_items_list.append(block[0])
            self.resume_btn_items_list.append(block[1])

        x = (HORIZONTAL_BLOCK_NUM-2) * BLOCK_WIDTH
        y = 2 * BLOCK_WIDTH
        block = self.draw_block(x, y)
        self.resume_btn_items_list.append(block[0])
        self.resume_btn_items_list.append(block[1])

        self.hide_resume_button()   # 刚开始先隐藏

    def show_pause_button(self):
        for item in self.pause_btn_items_list:
            item.setOpacity(0.04)

    def hide_pause_button(self):
        for item in self.pause_btn_items_list:
            item.setOpacity(0)

    def show_resume_button(self):
        for item in self.resume_btn_items_list:
            item.setOpacity(0.04)

    def hide_resume_button(self):
        for item in self.resume_btn_items_list:
            item.setOpacity(0)

    def draw_lose_text(self):
        item = QGraphicsSimpleTextItem()
        item.setText("  Game Over\n按R键重新开始")
        item.setScale(2.5)

        text_width = item.boundingRect().width()*item.scale()
        text_height = item.boundingRect().height()*item.scale()
        x = SCENE_WIDTH/2 - text_width/2
        y = SCENE_HEIGHT/2 - text_height/2
        item.setPos(x, y)

        self.addItem(item)
        self.lose_text_item = item
        self.hide_lose_text()

    def show_lose_text(self):
        self.lose_text_item.setOpacity(1)

    def hide_lose_text(self):
        self.lose_text_item.setOpacity(0)