import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import requests

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.line_edit = QLineEdit()            # 1
        self.text_browser = QTextBrowser()
        self.btn = QPushButton('爬取')

        self.line_edit.setPlaceholderText('待爬取的网址')
        self.text_browser.setPlaceholderText('爬取结果')
        self.btn.clicked.connect(self.crawl)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.line_edit)
        v_layout.addWidget(self.text_browser)
        v_layout.addWidget(self.btn)
        self.setLayout(v_layout)

        self.crawl_thread = CrawlThread(self)
        self.crawl_thread.result_signal.connect(self.show_result)

    def crawl(self):
        if not self.line_edit.text().strip():   # 2
            QMessageBox.critical(self, '错误', "请输入网址！")
            return

        if not self.crawl_thread.isRunning():
            self.crawl_thread.start()

    def show_result(self, text):
        self.text_browser.setPlainText(text)


class CrawlThread(QThread):
    result_signal = pyqtSignal(str)

    def __init__(self, window):
        super(CrawlThread, self).__init__()
        self.window = window

    def run(self):					            # 3
        url= self.window.line_edit.text().strip()
        result = requests.get(url)
        self.result_signal.emit(result.text)


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())