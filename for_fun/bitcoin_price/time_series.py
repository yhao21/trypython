import re, datetime
import numpy as np


def diff_lags(my_series, my_lags):
    '''
    compute price difference for n days
    my_series:
        This is a series you want deal with price diff
    my_lags:
        It stands for the length of period for price_diff.
        If my_lags = 1, then you compare price between yesterday and
        today.
            price_diff = p_t - p_{t-1}

        If my_se = 2, then
            price_diff = p_t - p_{t - 2}
    Usage:
        Suppose you want to see diff between each number in the series
        Code:
            my_se = [4,3,2,1]
            my_diff = diff_lags(my_se, 1)
        my_diff would be [-1,-1,-1]
        
        It actually do this:
            3-4 = -1    append to list
            2-3 = -1    append to list
            1-2 = -1    append to list
        
    '''
    diff_list = []
    period_index = 0
    last_value = my_series[0]
    for each_price in my_series:
            
        if period_index == my_lags :
            price_diff = each_price - last_value
            last_value = each_price
            #print(price_diff)
            # must reset the period_index, otherwise it
            # will blow up. And you only get one price_diff
            period_index = 0
            diff_list.append(price_diff)

        period_index += 1
    
    return diff_list





def make_lag(input_series, lag_num):
    '''
    create lag terms

    Suppose you have a price series [2,3,1,4,5], the last element stands for the current price
    the first element stands for the oldest price.

    if lag_num = 1, this fn will generate a lag1 list for you:
        [0,2,3,1,4]
    if lag_num = 2, this fn will generate a lag2 list for you:
        [0,0,2,3,1]
    Hence, you can form a dataframe below by your self:
    index   price   lag1    lag2
      0      2       0       0
      1      3       2       0
      2      1       3       2
      3      4       1       3
      4      5       4       1

    
    Usage:
        If you have a price series:
            price_series = [2,3,1,4,5]
        Use the following code to generate lag1
            price_lag1 = make_lag(price_series, 1)

        price_lag1 would be:
            [0,2,3,1,4]
    '''
    return [0]*lag_num + list(input_series[:-lag_num])












if __name__ == '__main__':
    pass

