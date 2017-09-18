import csv
from scrapy import Spider
from scrapy import Request
from datetime import datetime

class CursMdSpider(Spider):
    name = 'cursmd'

    start_urls = ['http://www.curs.md/ru/curs_valutar_banci']

    def parse(self, response):
        tableBody = response.xpath('//*[@id="tabelBankValute"]/tbody')

        now = datetime.now()
        ymd = '{}:{}:{}'.format(now.year, now.month, now.day)
        hms = '{}:{}:{}'.format(now.hour, now.minute, now.second)

        final_list_info = [['Date', ymd, hms]]

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

        max_usd_info = ['Buy usd']
        min_usd_info = ['Sell usd']
        max_eur_info = ['Buy eur']
        min_eur_info = ['Sell eur']
        max_rub_info = ['Buy rub']
        min_rub_info = ['Sell rub']
        max_ron_info = ['Buy ron']
        min_ron_info = ['Sell ron']
        max_uah_info = ['Buy uah']
        min_uah_info = ['Sell uah']
        max_gbp_info = ['Buy gbp']
        min_gbp_info = ['Sell gbp']
        max_chf_info = ['Buy chf']
        min_chf_info = ['Sell chf']


        all_data = []
        i = 2


        while True:
            bank_info = []
            break_while = None
            for row in tableBody:
                bank_name = row.xpath(
                        'normalize-space(//tr[' + str(i) + ']/td[1]/a)').extract()[0]
                # 1. BNM
                # 2. only in center bank
                # 3. Close or are different
                sup = row.xpath(
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


                # Add all info from one bank in list
                bank_info.append(i)
                bank_info.append(bank_name)
                bank_info.append(sup)
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


                # Add all banks info in one list
                all_data.append(bank_info)

                # Add all money to his list
                # Buy money to buy list
                # Sell money to sell list
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

                if not bank_name:
                    break_while = 'break'
                i += 1

            if break_while == 'break':
                break

        # Change , to . (split)
        # From 00,000 to 00.000 ( float )
        def change_to_dot(value):
            split_value = max(value).split(',')
            return split_value[0] + '.' + split_value[1]


        # Add to list all money to their lists
        def add_to_list(money, _list_with_data, _numb_from_td, _list_to_add_info):
            if max(money) in _list_with_data[_numb_from_td]:
                _list_to_add_info.append(bank_data[1])
                _list_to_add_info.append(float(change_to_dot(money)))
            

        # Get only maxminum value or only minumum value
        # With names of banks
        # And change , to .
        for bank_data in all_data:
            add_to_list(max_usd_list, bank_data, 3, max_usd_info)

            add_to_list(min_usd_list, bank_data, 4, min_usd_info)

            add_to_list(max_eur_list, bank_data, 5, max_eur_info)

            add_to_list(min_eur_list, bank_data, 6, min_eur_info)

            add_to_list(max_rub_list, bank_data, 7, max_rub_info)

            add_to_list(min_rub_list, bank_data, 8, min_rub_info)

            add_to_list(max_ron_list, bank_data, 9, max_ron_info)

            add_to_list(min_ron_list, bank_data, 10, min_ron_info)

            add_to_list(max_uah_list, bank_data, 11, max_uah_info)

            add_to_list(min_uah_list, bank_data, 12, min_uah_info)

            add_to_list(max_gbp_list, bank_data, 13, max_gbp_info)

            add_to_list(min_gbp_list, bank_data, 14, min_gbp_info)

            add_to_list(max_chf_list, bank_data, 15, max_chf_info)

            add_to_list(min_chf_list, bank_data, 16, min_chf_info)


        # Get only one maximum value if in list is many values
        def get_one_max_num(money_value):
            for money in money_value:
                if isinstance(money, float):
                    return money

        # Get only one minumum value if in list is many values
        def get_one_min_num(money_value):
            for money in money_value:
                if isinstance(money, float):
                    return money

        # value - value
        # Ex 2 - 1
        usd_result_total = get_one_max_num(max_usd_info) - get_one_min_num(min_usd_info)
        eur_result_total = get_one_max_num(max_eur_info) - get_one_min_num(min_eur_info)
        rub_result_total = get_one_max_num(max_rub_info) - get_one_min_num(min_rub_info)
        ron_result_total = get_one_max_num(max_ron_info) - get_one_min_num(min_ron_info)
        uah_result_total = get_one_max_num(max_uah_info) - get_one_min_num(min_uah_info)
        gbp_result_total = get_one_max_num(max_gbp_info) - get_one_min_num(min_gbp_info)
        chf_result_total = get_one_max_num(max_chf_info) - get_one_min_num(min_chf_info)


        # Print only for me
        def print_for_me(value, total, buy, sell):
            print(value + " %.2f" % total,
                    '|', 'B -', get_one_max_num(buy),
                    '|', 'S -', get_one_min_num(sell))

        print_for_me("USD", usd_result_total, max_usd_info, min_usd_info)
        print_for_me("EUR", eur_result_total, max_eur_info, min_eur_info)
        print_for_me("RUB", rub_result_total, max_rub_info, min_rub_info)
        print_for_me("RON", ron_result_total, max_ron_info, min_ron_info)
        print_for_me("UAH", uah_result_total, max_uah_info, min_uah_info)
        print_for_me("GBP", gbp_result_total, max_gbp_info, min_gbp_info)
        print_for_me("CHF", chf_result_total, max_chf_info, min_chf_info)

        # If value is > 0 we dont add it to csv
        if usd_result_total > 0:
            final_list_info.append(max_usd_info)
            final_list_info.append(min_usd_info)
            final_list_info.append(['Usd Total', "%.2f" % usd_result_total])
        elif eur_result_total > 0:
            final_list_info.append(max_eur_info)
            final_list_info.append(min_eur_info)
            final_list_info.append(['Eur Total', "%.2f" % eur_result_total])
        elif rub_result_total > 0:
            final_list_info.append(max_rub_info)
            final_list_info.append(min_rub_info)
            final_list_info.append(['Rub Total', "%.2f" % rub_result_total])
        elif ron_result_total > 0:
            final_list_info.append(max_ron_info)
            final_list_info.append(min_ron_info)
            final_list_info.append(['Ron Total', "%.2f" % ron_result_total])
        elif uah_result_total > 0:
            final_list_info.append(max_uah_info)
            final_list_info.append(min_uah_info)
            final_list_info.append(['Uah Total', "%.2f" % uah_result_total])
        elif gbp_result_total > 0:
            final_list_info.append(max_gbp_info)
            final_list_info.append(min_gbp_info)
            final_list_info.append(['Gbp Total', "%.2f" % gbp_result_total])
        elif chf_result_total > 0:
            final_list_info.append(max_chf_info)
            final_list_info.append(min_chf_info)
            final_list_info.append(['Chf Total', "%.2f" % chf_result_total])
        else:
            final_list_info.append(['Nothing today'])

        final_list_info.append([''])


        # Write to csv only file who has total result big than 0
        out = open('results.csv', 'a')

        for row in final_list_info:
            #print(row)
            for column in row:
                out.write('%s;' % column)
            out.write('\n')
        out.close()
