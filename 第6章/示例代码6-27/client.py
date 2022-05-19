import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *


class Client(QWidget):
    def __init__(self):
        super(Client, self).__init__()
        self.resize(600, 500)

        self.browser = QTextBrowser()               # 1
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

        self.udp = QUdpSocket()                     # 2
        data = f'{self.name}\n**%%加入%%**'
        self.udp.writeDatagram(data.encode(), QHostAddress('127.0.0.1'), 6666)
        self.udp.readyRead.connect(self.receive)
        self.browser.append('您已加入聊天。\n')

    def send(self):
        if not self.edit.toPlainText():
            return

        message = self.edit.toPlainText()
        data = f'{self.name}\n{message}\n'

        self.edit.clear()
        self.browser.append(data)
        self.udp.writeDatagram(data.encode(), QHostAddress('127.0.0.1'), 6666)

    def receive(self):				                # 3
        while self.udp.hasPendingDatagrams():
            data_size = self.udp.pendingDatagramSize()
            data, host, port = self.udp.readDatagram(data_size)
            if data:
                data = data.decode()
                self.browser.append(data)

    def closeEvent(self, event):			        # 4
        data = f'{self.name}\n**%%离开%%**'
        self.udp.writeDatagram(data.encode(), QHostAddress('127.0.0.1'), 6666)
        event.accept()


if __name__ == '__main__':
    app = QApplication([])
    client = Client()
    client.show()
    sys.exit(app.exec())