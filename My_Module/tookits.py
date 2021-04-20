import re, datetime
import numpy as np




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

