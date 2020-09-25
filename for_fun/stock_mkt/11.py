import pandas as pd
import numpy as np
import re, os
import datetime, time


def record_info(df, df_name, order):
    db = df[order]
    db.to_csv(df_name + '.csv')

class Stock:

    def __init__(self,stock_name,):
        self.stock = stock_name

    def transaction(self):
        if not os.path.exists('transaction.csv'):
            my_db = pd.DataFrame()
            record_info(my_db,'transaction', trans_order)

    # trans_order = ['status','Stock', 'Price','Volume','Value']
    def buy(self, buy_price, buy_volume):
        df = pd.read_csv(self.stock + 'csv')

        assert buy_price in list(df['Price']) is True, \
        '\n\nyou have to buy at what price people sell'

        value = buy_price * buy_volume
        new_info = pd.Series(['Buy', self.stock, buy_price, buy_volume, value])
        df = df.append(new_info, ignore_index = True)
        record_info(df, 'transaction', trans_order)



    def sell(self, sell_price, sell_volume):
        df = pd.read_csv(self.stock + '.csv')
        deal_time = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d')
        new_info = pd.Series([deal_time, self.stock, sell_price, sell_volume])
        df = df.append(new_info, ignore_index = True)
        record_info(df, self.stock, sell_order)



    def view(self):
        pass

    def create(self):
        df = pd.DataFrame()
        df.to_csv(self.stock + '.csv')
        print('\n\n' +self.stock + ' has been created sucessfully!')


class Market:

    def info(self):
        pass


    def graph(self):
        pass


def your_command():
    while True:
        init_com = input('\n\nwhat you want to do?\nnew stock[type: new]\nbuy stock[type: buy]\nsell stock[type: sell]\nexit program[type: quit]\ncommand: ')
        if init_com == 'new':
            stock_name = input('\n\ncreate a name for your stock: ')
            new_stock = Stock(stock_name).create()

        if init_com == 'sell':
            stock_name = input('\n\nwhich stock you want to sell: \ngo back to main menu [type: home]\ncommand: ')
            if stock_name == 'home':
                your_command()
            sell_price = input('\n\nsell at what price: \nchoose another stock[type: stock]\ngo back to main menu [type: home]\ncommand: ')
            if sell_price == 'home':
                your_command()
            if sell_price == 'stock':
                pass


        if init_com == 'quit':
            break

if __name__ == '__main__':
    sell_order = ['Date','Stock','Price','Volume']
    trans_order = ['status','Stock', 'Price','Volume','Value']
    mkt = pd.DataFrame()
    sell_mkt = pd.DataFrame()
    your_command()
