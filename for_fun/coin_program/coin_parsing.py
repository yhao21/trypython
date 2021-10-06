import os, glob
import pandas as pd
from bs4 import BeautifulSoup as bs

class Parsing():

    def __init__(self, folder_path):
        self.path = os.path.join(os.getcwd(), folder_path)
        self.df = pd.DataFrame()
        self.csv_name = 'coin_exchange.csv'


    def load_html(self):
        for one_file in glob.glob(os.path.join(self.path, '*.html')):
            with open(one_file, 'r', encoding = 'utf-8') as f:
                html = f.read()

            soup = bs(html, 'html.parser')
            self.parsing(soup)

        df_order = ['Name', 'Adj.Vol(24h)', 'Volume(24h)', 'Volume(7d)', 'Volume(30d)', 'No.Markets', 'Change(24h)']
        self.df = self.df[df_order]
        self.df.to_csv(os.path.join(os.getcwd(), self.csv_name))
        print(self.df)


    def parsing(self, content):
        trs = content.find_all('tr', {'class':'cmc-table-row'})
        for row in trs:
            tds = row.find_all('td')
            name = tds[1].find('a').string
            adj_vol_24 = tds[2].find('div').find('a').string
            vol_24 = tds[3].find('div').find('a').string
            vol_7 = tds[4].find('div').find('a').string
            vol_30 = tds[5].find('div').find('a').string
            No_mkt = tds[6].find('div').find('a').string
            change = tds[7].find('div').string
            self.df = self.df.append({
                'Name':name,
                'Adj.Vol(24h)':adj_vol_24,
                'Volume(24h)':vol_24,
                'Volume(7d)':vol_7,
                'Volume(30d)':vol_30,
                'No.Markets':No_mkt,
                'Change(24h)':change
            }, ignore_index = True)


if __name__ == '__main__':
    Parsing('main page').load_html()