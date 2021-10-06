import pandas as pd
import numpy as np
import time, datetime





class Stock():

    def __init__(self):
        self.df = mkt

    def sell(self,stock_name, sell_price,sell_volume):
        stock[stock_name]['volume'] = stock[stock_name]['volume'] - sell_volume
        post_time = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d-%H-%M-%S")

        self.df = self.df.append({
            '[time]':post_time,
            '[stock]': stock_name,
            '[selling price]': sell_price,
            '[volume]':int(self.df.iloc[-1,3]) + sell_volume
        },ignore_index=True)
        # self.df.sort_values(by = '[selling price]')


        return self.df




if __name__ == '__main__':

    stock = {
        'pubg':{'price':3,
                'volume':1000000},
        'Lol':{'price':5,
               'volume':200000}
    }

    col = ['[time]', '[stock]', '[selling price]', '[volume]']
    init_data = np.array(['2000-01-01','pubg',3.5,1000000]).reshape(1,4)
    mkt = pd.DataFrame(init_data, columns = col)

    mkt = Stock().sell('pubg',1.3,500)




    print(mkt)
    # print(type(mkt.iloc[1,2]))
    # print(type(mkt.iloc[0,2]))
