import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *


class Client(QWidget):
    def __init__(self):
        super(Client, self).__init__()
        self.resize(600, 500)

        self.browser = QTextBrowser()
        self.edit = QTextEdit()
        self.edit.setPlaceholderText('请输入消息')
        self.splitter = QSplitter(Qt.Vertical)
        self.splitter.addWidget(self.browser)
        self.splitter.addWidget(self.edit)
        self.splitter.setSizes([200, 100])

        self.send_btn = QPushButton('发送')
        self.send_btn.clicked.connect(self.send)

        v_layout = QVBoxLayout()
        v_layout.addWidget(self.splitter)
        v_layout.addWidget(self.send_btn)
        self.setLayout(v_layout)

        self.name = f'用户{id(self)}'
        print(f'我是{self.name}.')

        self.tcp = QTcpSocket()         # 1
        self.tcp.connectToHost(QHostAddress.LocalHost, 6666)
        self.tcp.connected.connect(self.handle_connection)
        self.tcp.readyRead.connect(self.receive)

    def handle_connection(self):
        self.browser.append('已连接到服务器！\n')
        self.browser.append('您已加入聊天。\n')

    def send(self):
        if not self.edit.toPlainText():
            return

        message = self.edit.toPlainText()
        data = f'{self.name}\n{message}\n'

        self.edit.clear()
        self.browser.append(data)
        self.tcp.write(data.encode())

    def receive(self):			        # 2
        while self.tcp.bytesAvailable():
            data_size = self.tcp.bytesAvailable()
            data = self.tcp.read(data_size)
            if data:
                self.browser.append(data.decode())

    def closeEvent(self, event):		# 3
        self.tcp.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication([])
    client = Client()
    client.show()
    sys.exit(app.exec())