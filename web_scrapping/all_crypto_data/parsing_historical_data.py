from bs4 import BeautifulSoup
import pandas as pd
import re, os, glob
import toolkits as tk





file_folder = 'history_csv'
if not os.path.exists(file_folder):
    os.mkdir(file_folder)

file_path = os.path.join('historical_data','*.html')
workload = len(glob.glob(file_path))
i = 1


for one_file in glob.glob(file_path):

    name = re.compile(r'historical_data/(.*).html').findall(one_file)[0]
    print(f'[{i}/{workload}] {name}')
    with open(one_file, 'r') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    
    table = soup.find('tbody')
    data = [[td.text.strip() for td in tr.findChildren('td')] for tr in table.findChildren('tr')]
    df = pd.DataFrame(data, columns = ['mktcap','vol','open_price','close_price'])
    
    date_data = [[th.text.strip() for th in tr.findChildren('th')] for tr in table.findChildren('tr')]
    df['date'] = pd.DataFrame(date_data, columns = ['date'])['date']
    df = df[['date','mktcap','vol','open_price','close_price']]
    df.drop([0], axis = 0, inplace = True)
    
    df['mktcap'] = [i.replace('$','').replace(',','') for i in df['mktcap'].values]
    df['vol'] = [i.replace('$','').replace(',','') for i in df['vol'].values]
    df['open_price'] = [i.replace('$','').replace(',','') for i in df['open_price'].values]
    df['close_price'] = [i.replace('$','').replace(',','') for i in df['close_price'].values]
    print(df)

    df.to_csv(os.path.join(file_folder, f'{name}.csv'), index = False)

    i += 1




