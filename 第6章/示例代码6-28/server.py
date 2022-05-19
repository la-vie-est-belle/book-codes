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

        self.tcp = QTcpServer()                     # 1
        if self.tcp.listen(QHostAddress.LocalHost, 6666):
            self.browser.append('已准备好与客户端进行连接。\n')
            self.tcp.newConnection.connect(self.handle_connection)
        else:
            error = self.tcp.errorString()
            self.browser.append(error)

        self.client_set = set()

    def handle_connection(self):                    # 2
        sock = self.tcp.nextPendingConnection()
        self.client_set.add(sock)
        sock.readyRead.connect(lambda: self.receive(sock))
        sock.disconnected.connect(lambda: self.handle_disconnection(sock))

        address, port = self.get_address_and_port(sock)
        data = f'{address}:{port}已加入聊天。\n'
        self.browser.append(data)
        self.send_to_other_clients(sock, data.encode())

    def receive(self, sock):
        while sock.bytesAvailable():
            data_size = sock.bytesAvailable()
            data = sock.read(data_size)
            self.send_to_other_clients(sock, data)

    def handle_disconnection(self, sock):
        self.client_set.remove(sock)

        address, port = self.get_address_and_port(sock)
        data = f'{address}:{port}离开。\n'
        self.browser.append(data)
        self.send_to_other_clients(sock, data.encode())

    def send_to_other_clients(self, current_client, data):
        for target in self.client_set:
            if target != current_client:
                target.write(data)
                address, port = self.get_address_and_port(target)
                self.browser.append(f'已将消息发送给{address}:{port}。\n')

    def get_address_and_port(self, sock):			# 3
        address = sock.peerAddress().toString()
        port = sock.peerPort()
        return address, port

    def closeEvent(self,event):
        self.tcp.close()
        event.accept()


if __name__ == '__main__':
    app = QApplication([])
    server = Server()
    server.show()
    sys.exit(app.exec())

