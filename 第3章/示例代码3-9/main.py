import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.mdi_area = QMdiArea()					                # 1

        self.new_btn = QPushButton('新建窗口')
        self.close_btn = QPushButton('关闭全部')
        self.tile_btn = QPushButton('平铺布局')
        self.cascade_btn = QPushButton('层叠布局')
        self.new_btn.clicked.connect(self.add_new_edit)		        # 2
        self.close_btn.clicked.connect(self.close_all)		        # 3
        self.tile_btn.clicked.connect(self.mdi_area.tileSubWindows)	# 4
        self.cascade_btn.clicked.connect(self.mdi_area.cascadeSubWindows)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.new_btn)
        v_layout.addWidget(self.close_btn)
        v_layout.addWidget(self.cascade_btn)
        v_layout.addWidget(self.tile_btn)
        v_layout.addWidget(self.mdi_area)
        self.setLayout(v_layout)

    def add_new_edit(self):
        new_edit = QTextEdit()
        sub_window = QMdiSubWindow()
        sub_window.setWidget(new_edit)
        self.mdi_area.addSubWindow(sub_window)
        sub_window.show()

    def close_all(self):
        self.mdi_area.closeAllSubWindows()
        all_windows = self.mdi_area.subWindowList()
        for window in all_windows:
            window.deleteLater()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())