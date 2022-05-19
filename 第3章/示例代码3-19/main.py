import sys
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.edit = QTextEdit()
        self.open_folder_btn = QPushButton('打开文件夹')
        self.open_file_btn = QPushButton('打开文件')
        self.save_as_btn = QPushButton('另存为')
        self.open_folder_btn.clicked.connect(self.open_folder)
        self.open_file_btn.clicked.connect(self.open_file)
        self.save_as_btn.clicked.connect(self.save_as)

        btn_h_layout = QHBoxLayout()
        window_v_layout = QVBoxLayout()
        btn_h_layout.addWidget(self.open_folder_btn)
        btn_h_layout.addWidget(self.open_file_btn)
        btn_h_layout.addWidget(self.save_as_btn)
        window_v_layout.addWidget(self.edit)
        window_v_layout.addLayout(btn_h_layout)
        self.setLayout(window_v_layout)

    def open_folder(self):      # 1
        folder_path = QFileDialog.getExistingDirectory(self, '打开文件夹', './')
        self.edit.setText(folder_path)

    def open_file(self):		# 2
        file_path, filter = QFileDialog.getOpenFileName(self, '打开文件', './', '文件 (*.txt *.log)')
        if file_path:
            with open(file_path, 'r') as f:
                self.edit.setText(f.read())

    def save_as(self):		    # 3
        save_path, filter = QFileDialog.getSaveFileName(self, '另存为', './', '文件 (*.txt *.log)')
        if save_path:
            with open(save_path, 'w') as f:
                f.write(self.edit.toPlainText())


if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())