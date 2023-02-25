import pandas as pd
import numpy as np


class PNL():
    def __init__(self):
        self.pnl = 0
        self.error = False

    def get_entry_price(self, entry_lsit):
        '''
        entry_list:     price and quantity you would like to put in your limit order. 
                        entry_list = [
                            [price1, quantity1],
                            [price2, quantity2],
                        ]
        '''
        pass

    def get_pnl(self, entry_price, quantity, trigger_list, long_short = 'long', detail = True):
        '''
        entry_price:    an entry price (float).
        quantity:       the size of your trading contract (float).
        trigger_list:   a list of take profit, or stop loss (list)
                        trigger_list = [
                            [price1, quantity1],
                            [price2, quantity2],
                        ]
        detail:         return profit and lost for each trigger price.
        '''
        self.check_trigger_list(quantity, trigger_list)


        pnl_list = []
        for one_trigger in trigger_list:
            if self.error == True:
                break

            trigger_price = one_trigger[0]
            trigger_size = one_trigger[1]
            trigger_pnl = (trigger_price - entry_price) * trigger_size
            #   one_trigger: [price1, quantity1]
            if long_short == 'short':
                trigger_pnl = - trigger_pnl
            self.pnl += trigger_pnl


            pnl_list.append([trigger_price, trigger_size, trigger_pnl])

        pnl_list.append(['-', '-', self.pnl])
                
        
        if detail:
            self.pnl_report(detail, pnl_list)
        else:
            self.pnl_report(detail, [self.pnl])

        
    def pnl_report(self, detail, pnl_list):
        if detail:
            df = pd.DataFrame(pnl_list, columns = ['trigger_price', 'trigger_size', 'PNL'])
            #df = df.append(pd.Series(['-', '-', self.pnl]), ignore_index = False)
        else:
            df = pd.DataFrame(pnl_list, columns = ['PNL'])
        print(df)

        


    
    def check_trigger_list(self, quantity, trigger_list):
        if np.sum([i[1] for i in trigger_list]) > quantity:
            print('Error: Triggered quantity is greater than the quantity of your current position.')
            self.error = True

if __name__ == '__main__':
    trigger_list = [
            [1250, 0.5],
            [1200, 0.4],
            [1100, 0.5],
            [1000, 0.3],
            #[],
            #[],
            ]
    PNL().get_pnl(1565, 1.8, trigger_list, long_short='short')

