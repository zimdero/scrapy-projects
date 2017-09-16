from scrapy import Spider
from scrapy import Request

class CursMdSpider(Spider):
    name = 'cursmd'

    start_urls = ['http://www.curs.md/ru/curs_valutar_banci']

    def parse(self, response):
        tableBody = response.xpath('//*[@id="tabelBankValute"]/tbody')
        i = 1
        while True:
            break_while = None
            for row in tableBody:
                bank_name = row.xpath('normalize-space(//tr[' + str(i) + ']/td[1]/a)').extract()[0]
                bnm = row.xpath('normalize-space(//tr[' + str(i) + ']/td[1]/sup)').extract()[0]
                buy_usd = row.xpath('normalize-space(//tr[' + str(i) + ']/td[2])').extract()[0]
                sell_usd = row.xpath('normalize-space(//tr[' + str(i) + ']/td[3])').extract()[0]
                print(i, bank_name, bnm, buy_usd, sell_usd)
                if not bank_name:
                    break_while = 'break'
                i += 1

            if break_while == 'break':
                break
