import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.web_view = QWebEngineView()                    # 1
        self.web_view.load(QUrl('https://www.baidu.com'))
        self.web_view.loadStarted.connect(self.start)
        self.web_view.loadProgress.connect(self.progress)
        self.web_view.loadFinished.connect(self.finish)
        self.web_view.urlChanged.connect(self.show_url)

        self.btn = QPushButton('更改网址')                  # 2
        self.btn.clicked.connect(self.change_url)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.web_view)
        v_layout.addWidget(self.btn)
        self.setLayout(v_layout)

    def start(self):
        print('开始加载')

    def progress(self, value):
        print(value)

    def finish(self):
        print('加载结束')
        print(self.web_view.title())
        print(self.web_view.icon())

    def show_url(self):
        print(self.web_view.url())

    def change_url(self):
        self.web_view.setUrl(QUrl('https://www.ptpress.com.cn/'))


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())