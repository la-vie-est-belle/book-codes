import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.value = 0				                # 1

        self.timer = QTimer()
        self.timer.start(100)
        self.timer.timeout.connect(self.update_progress)

        self.progress_bar1 = QProgressBar()
        self.progress_bar1.setRange(0, 0)

        self.progress_bar2 = QProgressBar()
        self.progress_bar2.setTextVisible(False)	# 2
        self.progress_bar2.setMinimum(0)
        self.progress_bar2.setMaximum(0)
        self.progress_bar2.setInvertedAppearance(True)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.progress_bar1)
        v_layout.addWidget(self.progress_bar2)
        self.setLayout(v_layout)

    def update_progress(self):
        self.value += 1
        self.progress_bar1.setValue(self.value)
        self.progress_bar2.setValue(self.value)

        if self.value == 100:
            self.timer.stop()


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())