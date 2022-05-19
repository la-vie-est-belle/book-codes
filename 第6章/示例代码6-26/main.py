import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.resize(1000, 600)
        self.url_input = QLineEdit()            # 1
        self.back_btn = QPushButton()
        self.forward_btn = QPushButton()
        self.refresh_btn = QPushButton()
        self.zoom_in_btn = QPushButton()
        self.zoom_out_btn = QPushButton()
        self.web_view = QWebEngineView()

        self.init_ui()

    def init_ui(self):
        self.init_widgets()
        self.init_signals()
        self.init_layouts()

    def init_widgets(self):
        self.back_btn.setEnabled(False)
        self.forward_btn.setEnabled(False)
        self.back_btn.setIcon(QIcon('back.png'))
        self.forward_btn.setIcon(QIcon('forward.png'))
        self.refresh_btn.setIcon(QIcon('refresh.png'))
        self.zoom_in_btn.setIcon(QIcon('zoom-in.png'))
        self.zoom_out_btn.setIcon(QIcon('zoom-out.png'))
        self.url_input.setText('about:blank')
        self.url_input.setPlaceholderText('请输入网址')
        self.web_view.setUrl(QUrl('about:blank'))

    def init_signals(self):			            # 2
        self.back_btn.clicked.connect(self.web_view.back)
        self.forward_btn.clicked.connect(self.web_view.forward)
        self.refresh_btn.clicked.connect(self.web_view.reload)
        self.zoom_in_btn.clicked.connect(self.zoom_in)
        self.zoom_out_btn.clicked.connect(self.zoom_out)
        self.web_view.loadFinished.connect(self.update_state)

    def init_layouts(self):
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        h_layout.addWidget(self.back_btn)
        h_layout.addWidget(self.forward_btn)
        h_layout.addWidget(self.refresh_btn)
        h_layout.addWidget(self.url_input)
        h_layout.addWidget(self.zoom_in_btn)
        h_layout.addWidget(self.zoom_out_btn)
        v_layout.addLayout(h_layout)
        v_layout.addWidget(self.web_view)
        v_layout.setContentsMargins(0, 8, 0, 0)
        self.setLayout(v_layout)

    def update_state(self):
        url = self.web_view.url().toString()
        self.url_input.setText(url)

        if self.web_view.history().canGoBack():
            self.back_btn.setEnabled(True)
        else:
            self.back_btn.setEnabled(False)

        if self.web_view.history().canGoForward():
            self.forward_btn.setEnabled(True)
        else:
            self.forward_btn.setEnabled(False)

    def zoom_in(self):
        zoom_factor = self.web_view.zoomFactor()
        self.web_view.setZoomFactor(zoom_factor + 0.1)

    def zoom_out(self):
        zoom_factor = self.web_view.zoomFactor()
        self.web_view.setZoomFactor(zoom_factor - 0.1)

    def keyPressEvent(self, event):             # 3
        if event.key()==Qt.Key_Return or event.key()==Qt.Key_Enter:
            if not self.url_input.hasFocus():
                return

            url = self.url_input.text()
            if url.startswith('https://') or url.startswith('http://'):
                self.web_view.load(QUrl(url))
            else:
                url = 'https://' + url
                self.web_view.load(QUrl(url))

            self.url_input.setText(url)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())