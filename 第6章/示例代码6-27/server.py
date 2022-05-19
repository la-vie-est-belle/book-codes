import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtNetwork import *


class Server(QWidget):
    def __init__(self):
        super(Server, self).__init__()
        self.resize(400, 200)
        self.browser = QTextBrowser()
        v_layout = QVBoxLayout()
        v_layout.addWidget(self.browser)
        self.setLayout(v_layout)

        self.udp = QUdpSocket()             # 1
        if self.udp.bind(QHostAddress.LocalHost, 6666):
            self.browser.append('已准备好接收数据.\n')
            self.udp.readyRead.connect(self.receive)

        self.client_set = set()

    def receive(self):
        while self.udp.hasPendingDatagrams():
            data_size = self.udp.pendingDatagramSize()
            data, host, port = self.udp.readDatagram(data_size)

            host = host.toString()          # 2
            data = data.decode()
            message = data.split('\n')[1]
            if message == '**%%加入%%**':
                self.client_set.add((host, port))
                data = f'{host}:{port}已加入聊天。\n'
                self.browser.append(data)
            elif message == '**%%离开%%**':
                self.client_set.remove((host, port))
                data = f'{host}:{port}已离开。\n'
                self.browser.append(data)
            else:
                self.browser.append(f'收到一条来自{host}:{port}的消息。\n')

            self.send_to_other_clients((host, port), data.encode())

    def send_to_other_clients(self, current_client, data):
        for target in self.client_set:
            if target != current_client:
                host = target[0]
                port = target[1]
                self.udp.writeDatagram(data, QHostAddress(host), port)
                self.browser.append(f'已将消息发送给{host}:{port}。\n')

    def closeEvent(self,event):		        # 3
        self.udp.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication([])
    server = Server()
    server.show()
    sys.exit(app.exec())

