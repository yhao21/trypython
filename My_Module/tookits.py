import re, datetime
import numpy as np


def compute_n_lag_return(my_series, my_lags):
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
            my_diff = compute_n_lag_return(my_se, 1)
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
            print(price_diff)
            # must reset the period_index, otherwise it
            # will blow up. And you only get one price_diff
            period_index = 0
            diff_list.append(price_diff)

        period_index += 1
    
    return diff_list









def get_power(input_num, base_numb):
    '''
    state with:   base^n = x
    take log at both side:
        n*log(base) = log(x)
        n = log(x)/log(base)
    example:
        we want to comput n in 2^n = 8
        n = log(8)/log(2)
          = 3

    Usage:
        power_number = get_power(input_num = 8, base_numb = 2)
    '''

    return np.log(input_num)/np.log(base_numb)





def to_num(df_string):
    """
    trans string form into numbers.
    for example:
        '5,221.01'  ---->    5221.01
           str                float

        a = '5,221.01'
        b = to_num(a)

    """

    before = ''
    if re.compile(r'\.').findall(df_string) == []:
        int_part = re.compile(r'(\w+)').findall(df_string)
        if len(int_part) == 1:
            item = int(df_string)
        else:
            for i in range(len(int_part)):
                before += int_part[i]
            item = int(before)

    if re.compile(r'\.').findall(df_string) != []:

        int_part = re.compile(r'(\w+)').findall(df_string)
        power = len(int_part[-1])
        after = int(int_part[-1])
        for i in range(len(int_part) -1 ):
            before = before + int_part[i]
        before = int(before)
        item = before + after * (10 ** -power)

    return item


def strdate(str_date):
    """
    trans str form date into datetime form. so that you can compare the value
    for example:

    date = strdate('Jun 26, 2020')
    """
    items = re.compile(r'\w+').findall(str_date)
    month_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    month_index = [1,2,3,4,5,6,7,8,9,10,11,12]
    dt = []
    for mon in items:
        if mon in month_list:
            index = month_list.index(mon)
            month_val = month_index[index]
            dt.append(month_val)
        if len(mon) == 2:
            day_val = int(mon)
            dt.append(day_val)
        if len(mon) == 4:
            year_val = int(mon)
            dt.append(year_val)
    reform_date = datetime.datetime(dt[2], dt[0],dt[1]).strftime('%Y-%m-%d')

    return reform_date








if __name__ == '__main__':
    a = to_num('123,331,212.121')
    b = strdate('Jun 26, 2020')
    print(b)

