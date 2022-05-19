import requests
from parsel import Selector
from PyQt5.QtCore import *


class CrawlThread(QThread):
    log_signal = pyqtSignal(str)
    finish_signal = pyqtSignal()
    data_signal = pyqtSignal(list)

    def __init__(self, window):
        super(CrawlThread, self).__init__()
        self.window = window
        self.flag = True

    def run(self):
        page_count = 0
        total_page = self.window.page_spin_box.value()

        self.flag = True
        while page_count < total_page:
            if self.flag:
                page_count += 1
                self.crawl_page(page_count)
            else:
                break

        self.finish_signal.emit()

    def crawl_page(self, page_num):
        self.log_signal.emit(f'当前正在爬取第{page_num}页')

        page_url = f'https://quotes.toscrape.com/page/{page_num}/'
        response = requests.get(page_url)

        if 'No quotes found!' in response.text:
            self.log_signal.emit('当前页面上没有名言了，不再继续爬取。')
            self.stop()
            return

        selector = Selector(response.text)
        quotes = selector.xpath('//div[@class="quote"]')

        for quote in quotes:
            content = quote.xpath('./span/text()').extract_first()
            author = quote.xpath('./span/small/text()').extract_first()
            tags = quote.xpath('./div[@class="tags"]/a/text()').extract()
            tags = ';'.join(tags)
            print([content, author, tags])
            self.data_signal.emit([content, author, tags])

    def stop(self):
        self.flag = False