import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(300, 300)
        toolbar1 = QToolBar('工具栏1')			        # 1
        toolbar2 = QToolBar('工具栏2')

        open_action = QAction(QIcon('open.ico'), '打开', self)
        save_action = QAction(QIcon('save.ico'), '保存', self)
        quit_action = QAction(QIcon('quit.ico'), '退出', self)

        toolbar1.addAction(open_action)
        toolbar1.addAction(save_action)
        toolbar1.addSeparator()
        toolbar1.addAction(quit_action)
        toolbar2.addAction(open_action)
        toolbar2.addAction(save_action)
        toolbar2.addSeparator()
        toolbar2.addAction(quit_action)

        # 2
        toolbar1.setAllowedAreas(Qt.TopToolBarArea|Qt.BottomToolBarArea)
        toolbar2.setMovable(False)

        self.addToolBar(Qt.TopToolBarArea, toolbar1)	# 3
        self.addToolBar(Qt.BottomToolBarArea, toolbar2)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())