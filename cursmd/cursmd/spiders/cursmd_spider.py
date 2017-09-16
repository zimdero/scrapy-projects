import csv
from scrapy import Spider
from scrapy import Request

class CursMdSpider(Spider):
    name = 'cursmd'

    start_urls = ['http://www.curs.md/ru/curs_valutar_banci']

    def parse(self, response):
        tableBody = response.xpath('//*[@id="tabelBankValute"]/tbody')
        max_usd_list = []
        min_usd_list = []
        max_eur_list = []
        min_eur_list = []
        max_rub_list = []
        min_rub_list = []
        max_ron_list = []
        min_ron_list = []
        max_uah_list = []
        min_uah_list = []
        max_gbp_list = []
        min_gbp_list = []
        max_chf_list = []
        min_chf_list = []
        max_try_list = []
        min_try_list = []

        max_usd_info = []
        min_usd_info = []
        max_eur_info = []
        min_eur_info = []

        final_info = []
        final_info_first_line = [
                'Bank name', 'Max usd', 'Min usd'
                ]
        final_info.append(final_info_first_line)
        all_data = []
        first_line = [
                'Nr', 'Bank Name', 'Info', 'Usd buy', 'Usd sell',
                'Eur buy', 'Eur sell', 'Rub buy', 'Rub sell',
                'Ron buy', 'Ron sell', 'Uah buy', 'Uah sell', 
                'Gbp buy', 'Gbp sell', 'Chf buy', 'Chf sell'
                ]
        all_data.append(first_line)
        i = 2
        j = 0


        while True:
            bank_info = []
            break_while = None
            for row in tableBody:
                bank_name = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[1]/a)').extract()[0]
                bnm = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[1]/sup)').extract()[0]
                buy_usd = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[2])').extract()[0]
                sell_usd = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[3])').extract()[0]
                buy_eur = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[4])').extract()[0]
                sell_eur = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[5])').extract()[0]
                buy_rub = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[6])').extract()[0]
                sell_rub = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[7])').extract()[0]
                buy_ron = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[8])').extract()[0]
                sell_ron = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[9])').extract()[0]
                buy_uah = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[10])').extract()[0]
                sell_uah = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[11])').extract()[0]
                buy_gbp = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[12])').extract()[0]
                sell_gbp = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[13])').extract()[0]
                buy_chf = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[14])').extract()[0]
                sell_chf = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[15])').extract()[0]
                buy_try = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[16])').extract()[0]
                sell_try = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[17])').extract()[0]
                #print(i, bank_name, bnm, 
                #        buy_usd, sell_usd, 
                #        buy_eur, sell_eur,
                #        buy_rub, sell_rub,
                #        buy_ron, sell_ron,
                #        buy_uah, sell_uah,
                #        buy_gbp, sell_gbp,
                #        buy_chf, sell_chf,
                #        buy_try, sell_try
                #        )
                bank_info.append(i)
                bank_info.append(bank_name)
                bank_info.append(bnm)
                bank_info.append(buy_usd)
                bank_info.append(sell_usd)
                bank_info.append(buy_eur)
                bank_info.append(sell_eur)
                bank_info.append(buy_rub)
                bank_info.append(sell_rub)
                bank_info.append(buy_ron)
                bank_info.append(sell_ron)
                bank_info.append(buy_uah)
                bank_info.append(sell_uah)
                bank_info.append(buy_gbp)
                bank_info.append(sell_gbp)
                bank_info.append(buy_chf)
                bank_info.append(sell_chf)
                bank_info.append(buy_try)
                bank_info.append(sell_try)


                all_data.append(bank_info)

                if buy_usd and sell_ron != '-':
                    max_usd_list.append(buy_usd)

                if sell_usd and sell_ron != '-':
                    min_usd_list.append(sell_usd)

                if buy_eur and sell_ron != '-':
                    max_eur_list.append(buy_eur)

                if sell_eur and sell_ron != '-':
                    min_eur_list.append(sell_eur)

                if buy_rub and sell_ron != '-':
                    max_rub_list.append(buy_rub)

                if sell_rub and sell_ron != '-':
                    min_rub_list.append(sell_rub)

                if buy_ron and sell_ron != '-':
                    max_ron_list.append(buy_ron)

                if sell_ron and sell_ron != '-':
                    min_ron_list.append(sell_ron)

                if buy_uah and sell_ron != '-':
                    max_uah_list.append(buy_uah)

                if sell_uah and sell_uah != '-':
                    min_uah_list.append(sell_uah)

                if buy_gbp and sell_gbp != '-':
                    max_gbp_list.append(buy_gbp)

                if sell_gbp and sell_gbp != '-':
                    min_gbp_list.append(sell_gbp)

                if buy_chf and sell_chf != '-':
                    max_chf_list.append(buy_chf)

                if sell_chf and sell_chf != '-':
                    min_chf_list.append(sell_chf)

                if buy_chf and sell_chf != '-':
                    max_chf_list.append(buy_chf)

                if sell_try and sell_try != '-':
                    min_chf_list.append(sell_chf)

                if not bank_name:
                    break_while = 'break'
                i += 1

            if break_while == 'break':
                break

        print(
                max(max_usd_list), min(min_usd_list),
                max(max_eur_list), min(min_eur_list),
                max(max_rub_list), min(min_rub_list),
                max(max_ron_list), min(min_ron_list),
                max(max_uah_list), min(min_uah_list),
                max(max_gbp_list), min(min_gbp_list),
                max(max_chf_list), min(min_chf_list),
                )


        for bank_data in all_data:
            if max(max_usd_list) in bank_data[3]:
                max_usd_info.append(bank_data[1])
                max_usd_info.append(max(max_usd_list))

            if min(min_usd_list) in bank_data[4]:
                min_usd_info.append(bank_data[1])
                min_usd_info.append(min(min_usd_list))

            if max(max_eur_list) in bank_data[5]:
                max_eur_info.append(bank_data[1])
                max_eur_info.append(max(max_eur_list))

            if min(min_eur_list) in bank_data[6]:
                min_eur_info.append(bank_data[1])
                min_eur_info.append(min(min_eur_list))

        print(
                max_usd_info,
                min_usd_info,
                max_eur_info,
                min_eur_info,
                )
        out = open('results.csv', 'w')

        for row in all_data:
            for column in row:
                out.write('%s;' % column)
            out.write('\n')
        out.close()
