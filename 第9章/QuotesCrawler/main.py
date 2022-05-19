import sys
from PyQt5.QtWidgets import *
from window import CrawlWindow
from qt_material import apply_stylesheet


if __name__ == '__main__':
    app = QApplication([])
    apply_stylesheet(app, theme='dark_teal.xml')
    crawl_window = CrawlWindow()
    crawl_window.show()
    sys.exit(app.exec())


