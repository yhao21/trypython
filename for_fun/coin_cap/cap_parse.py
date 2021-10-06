from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re, datetime

#
# df = pd.DataFrame()
#
# with open('cap.html', 'r', encoding = 'utf-8') as f:
#     html = f.read()
#
# soup = BeautifulSoup(html,'html.parser')
# rows = soup.find_all('tr', {'class':'cmc-table-row'})
# for row in rows:
#     tds = row.find_all('td')
#     date_ = tds[0].string
#     open_p = tds[1].string
#     high_p = tds[2].string
#     low_p = tds[3].string
#     close_p = tds[4].string
#     volume = tds[5].string
#     mkt_cap = tds[6].string
#     df = df.append({
#         'Date':date_,
#         'Open':open_p,
#         'High':high_p,
#         'Low':low_p,
#         'Close':close_p,
#         'Volume':volume,
#         'Market Cap':mkt_cap
#     },ignore_index = True)
# order = ['Date','Open','High','Low','Close','Volume','Market Cap']
# df = df[order]
# df.sort_values(by='Date',ascending = True)
# df.to_csv('bitcon.csv',index=False)
# print(df)
#

def to_num(df_string):

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



df = pd.read_csv('bitcon.csv')
open = np.array([to_num(i) for i in df.iloc[:,1].values]).reshape(len(df.iloc[:,1].values),1)
date = np.array([strdate(i) for i in df.iloc[:,0].values]).reshape(len(df.iloc[:,0].values),1)
form = pd.DataFrame(np.hstack((date,open)), columns = ['date','open'])
form = form.sort_values(by='date')


print(form)


date = [i for i in form.iloc[:,0].values]
open = [float(i) for i in form.iloc[:,1].values]
plt.plot(date,open)
plt.show()
print(date)