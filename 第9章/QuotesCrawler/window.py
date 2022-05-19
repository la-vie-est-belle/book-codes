from PyQt5.QtGui import *
from PyQt5.QtSql import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

from crawl import CrawlThread
from sound import AudioSource


class CrawlWindow(QWidget):
    def __init__(self):
        super(CrawlWindow, self).__init__()
        self.resize(800, 600)
        self.setWindowTitle('名人名言爬取软件')
        self.setWindowIcon(QIcon('./res/icon.ico'))

        self.table = QTableWidget()             # 显示爬取内容
        self.browser = QTextBrowser()           # 输出爬取日志
        self.page_spin_box = QSpinBox()         # 设置爬取页数
        self.start_stop_btn = QPushButton()     # 开始停止爬取
        self.save_btn = QPushButton()           # 保存爬取内容

        self.audio_source = AudioSource()       # 音频播放
        self.crawl_thread = CrawlThread(self)   # 爬虫线程
        self.init_ui()                          # 设置界面

    def init_ui(self):
        self.init_widgets()
        self.init_signals()
        self.init_layouts()

    def init_widgets(self):
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['名言', '作者', '标签'])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setAlternatingRowColors(True)

        self.page_spin_box.setValue(1)
        self.start_stop_btn.setText('开始爬取')
        self.save_btn.setText('保存结果')

    def init_signals(self):
        self.start_stop_btn.clicked.connect(self.crawl)
        self.crawl_thread.log_signal.connect(self.show_log)
        self.crawl_thread.finish_signal.connect(self.finished)
        self.crawl_thread.data_signal.connect(self.set_data_on_table)
        self.save_btn.clicked.connect(self.save)

    def init_layouts(self):
        h_layout = QHBoxLayout()
        v_layout = QVBoxLayout()
        h_layout.addWidget(QLabel('设置爬取页数：'))
        h_layout.addWidget(self.page_spin_box)
        h_layout.addStretch()
        h_layout.addWidget(self.start_stop_btn)
        h_layout.addWidget(self.save_btn)
        v_layout.addWidget(self.table)
        v_layout.addWidget(self.browser)
        v_layout.addLayout(h_layout)
        self.setLayout(v_layout)

    def crawl(self):
        if self.start_stop_btn.text() == '开始爬取':
            self.start_crawling()
        else:
            self.stop_crawling()

    def start_crawling(self):
        self.audio_source.play_audio('button')

        self.table.setRowCount(0)
        self.browser.clear()
        self.show_log('开始爬取')
        self.start_stop_btn.setText('停止爬取')

        if not self.crawl_thread.isRunning():
            self.crawl_thread.start()

    def stop_crawling(self):
        self.audio_source.play_audio('button')

        self.show_log('正在停止爬取')
        self.start_stop_btn.setText('正在停止...')
        self.start_stop_btn.setEnabled(False)
        self.crawl_thread.stop()

    def finished(self):
        self.audio_source.play_audio('finish')
        self.show_log('爬取结束')
        self.start_stop_btn.setText('开始爬取')
        self.start_stop_btn.setEnabled(True)

    def show_log(self, log):
        self.browser.append(log)
        self.browser.moveCursor(QTextCursor.End)

    def set_data_on_table(self, data):
        row_count = self.table.rowCount()
        self.table.setRowCount(row_count + 1)

        for i in range(3):
            item = QTableWidgetItem()
            item.setText(data[i])
            item.setTextAlignment(Qt.AlignCenter)
            self.table.setItem(row_count, i, item)
            self.table.scrollToBottom()

    def save(self):
        self.audio_source.play_audio('button')
        path, _ = QFileDialog.getSaveFileName(self, '保存', './', '(*.txt *.db)')
        if not path:
            return

        format = path.split('.')[-1]
        if format == 'txt':
            self.save_to_txt(path)
        elif format == 'db':
            self.save_to_db(path)

        self.audio_source.play_audio('saved')
        QMessageBox.information(self, '提示', '保存成功！')

    def save_to_txt(self, path):
        row_count = self.table.rowCount()

        data = []
        for row in range(row_count):
            quote = self.table.item(row, 0).text()
            author = self.table.item(row, 1).text()
            tags = self.table.item(row, 2).text()
            data.append(f"名言：{quote}\n作者：{author}\n标签：{tags}")

        print(data)
        with open(path, 'w') as f:
            f.write('\n\n'.join(data))

    def save_to_db(self, path):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName(path)
        if not db.open():
            error = db.lastError().text()
            QMessageBox.critical(self, 'Database Connection', error)
            return

        # 创建数据表
        query = QSqlQuery()
        query.exec("""
            CREATE TABLE Quotes (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            quote   TEXT    NOT NULL,
            author  TEXT    NOT NULL,
            tags    TEXT    NOT NULL);
        """)

        # 插入数据
        row_count = self.table.rowCount()
        for row in range(row_count):
            quote = self.table.item(row, 0).text()
            author = self.table.item(row, 1).text()
            tags = self.table.item(row, 2).text()

            query.prepare("""
                INSERT INTO Quotes (quote, author, tags)
                VALUES (?, ?, ?);
            """)
            query.addBindValue(quote)
            query.addBindValue(author)
            query.addBindValue(tags)
            query.exec()

        db.close()

