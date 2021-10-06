import os, glob, re, time
from bs4 import BeautifulSoup
from time_countdown import workload_time_left as wtl
import pandas as pd




class Parsing():
    def __init__(self, folder):
        # it should be a string, i.e., 'coinmktcap_html_file'
        self.path = os.getcwd()
        self.folder = folder
        # determine whether parse deeplink. False by default
        self.df = pd.DataFrame()
        self.file_path = None
        self.deeplink = ''
        self.deep_scrapping_url = []



    def init_file(self):
        '''
        Determine which file(s) to parse.
        '''

        # /home/synferlo/git/trypython/4980_Machine_Learning/midterm/code/coinmktcap_html_file
        self.file_path = os.path.join(self.path, self.folder)



    def output_format(self, output):
        '''
        Format output in when you print in terminal
        '''

        return ' [ ' + str(output)  + ' ] '



    def parsing_coin_html(self):
        '''
        Parsing coinmktcap html files
        '''

        self.init_file()

        total_workload = len(glob.glob(self.file_path + '/*.html'))
        workload = len(glob.glob(self.file_path + '/*.html'))
        
        for one_file in glob.glob(self.file_path + '/*.html'):

            start_time = time.time()
            # first round: 1_15, last round: 192_15
            rep_round = re.compile(r'(\d*_15)_page').findall(one_file)[0]

            with open(one_file, 'r') as f:
                html = f.read()
            
            soup = BeautifulSoup(html, 'html.parser')
            rows = soup.find('tbody').find_all('tr', \
                    {'class':'rc-table-row rc-table-row-level-0 cmc-table-row'})
            
            for row in rows:
                tds = row.find_all('td')
                rank = tds[1].find('p').string
                name = tds[2].find('div').find('p').string.replace(' ','').lower()
                abbrev = tds[2].find('div').find('p', \
                        {'class':'Text-sc-1eb5slv-0 eweNDy coin-item-symbol'}).string
                price = tds[3].find('div').find('a').string.replace('$','').replace(',','')
                volume = tds[7].find('a').find('p').string.replace('$', '').replace(',','')
                mktcap = tds[6].find('p').string.replace('$', '').replace(',','')

                # identify which round you are. first 15mins with '1', last 15 mins with '192'
                repetition = re.compile(r'(\d*)_15') .findall(rep_round)[0]


                # regex return repetition as str, be careful
                if repetition == '1':
                    url_base = 'https://coinmarketcap.com'
                    link_base = tds[2].find('a')['href']
                    self.deeplink = url_base + link_base
                    self.deep_scrapping_url.append(self.deeplink)


                self.df = self.df.append({
                    'repetition':repetition,
                    'rank':rank,
                    'name':name,
                    'price':price,
                    'abbr':abbrev,
                    '24hr_volume': volume,
                    'mktcap':mktcap,
                    'deeplink':self.deeplink
                    },ignore_index = True)

                self.deeplink = ''


            round_time = time.time() - start_time
            print('parsing' + self.output_format('CoinMKT_file') + '-' * 100 + '(%s/%s)' % (total_workload - workload + 1, total_workload))
            wtl(round_time, 0, workload - 1)
            print('\n\n')
            workload -= 1


        order = ['repetition','rank', 'name', 'abbr', 'price', '24hr_volume', 'mktcap', 'deeplink']
        self.df = self.df[order]
        print(self.df)
        self.df.to_csv('CoinMKT_48hrs_data.csv')
        print('\nNB: Prepare' + self.output_format(len(self.deep_scrapping_url)) + 'deeplink URLs for you.\n\n')


        return self.deep_scrapping_url




    def parsing_gecko_html(self):
        '''
        Parsing coingecko html files
        '''

        self.init_file()

        total_workload = len(glob.glob(self.file_path + '/*.html'))
        workload = len(glob.glob(self.file_path + '/*.html'))

        for one_file in glob.glob(self.file_path + '/*.html'):

            start_time = time.time()
            # first round: 1_15, last round: 192_15
            rep_round = re.compile(r'(\d*_15)_page').findall(one_file)[0]

            with open(one_file, 'r') as f:
                html = f.read()

            rows = BeautifulSoup(html, 'html.parser').find('tbody').find_all('tr')
            for row in rows:
                tds = row.find_all('td')
                rank = re.compile(r'\d*').findall(tds[1].string)[1]
                # ['', 'Bitcoin',  'Diamond' ,'']
                name_frac = re.compile(r'(\w*)').findall(tds[2].find('a',\
                        {'class':'d-none d-lg-flex font-bold align-items-center justify-content-between'}).string.replace(' ','').lower())
                name = name_frac[1]
                for name_char in name_frac[2:]:
                    if name_char != '':
                        name += name_char

                abbr_frac = re.compile(r'\w*').findall(tds[2].find('a', \
                        {'class':'d-lg-none font-bold'}).string.replace(' ',''))
                abbr = abbr_frac[1]
                for abbr_char in abbr_frac[2:]:
                    if abbr_char != '':
                        abbr += abbr_char
                
                price = tds[3].find('span').string.replace('$','').replace(',','')

                try:
                    volume = tds[7].find('span').string.replace('$','').replace(',','')
                except:
                    # if no information, 0
                    volume = 0
                mktcap = tds[8].find('span').string.replace('$','').replace(',','')
                repetition = re.compile(r'(\d*)_15').findall(rep_round)[0]

                if repetition == '1':
                    url_base = 'https://www.coingecko.com'
                    link_base = tds[2].find('a',{'class':'d-lg-none font-bold'})['href']
                    self.deeplink = url_base + link_base
                    self.deep_scrapping_url.append(self.deeplink)
                    



                self.df = self.df.append({
                    'repetition':repetition,
                    'rank':rank,
                    'name':name,
                    'price':price,
                    'abbr':abbr,
                    '24hr_volume':volume,
                    'mktcap':mktcap,
                    'deeplink':self.deeplink
                    },ignore_index = True)

                self.deeplink = ''

            round_time = time.time() - start_time
            print('parsing' + self.output_format('Gecko_file') + '-' * 100 + '(%s/%s)' % (total_workload - workload + 1, total_workload))
            wtl(round_time, 0, workload - 1)
            print('\n\n')
            workload -= 1

            
        order = ['repetition','rank', 'name', 'abbr', 'price', '24hr_volume', 'mktcap', 'deeplink']
        self.df = self.df[order]
        print(self.df)
        self.df.to_csv('Gecko_48hrs_data.csv')
        print('\nNB: Prepare' + self.output_format(len(self.deep_scrapping_url)) + 'deeplink URLs for you.\n\n')


        return self.deep_scrapping_url





if __name__ == '__main__':
    folder = 'coinmktcap_html_file'
    coinmkt_parse_and_deeplink = Parsing(folder).parsing_coin_html()
    folder = 'gecko_html_file'
    gecko_parse_and_deeplink = Parsing(folder).parsing_gecko_html()

    deeplink_list = [(coin, gecko) for coin, gecko in zip(coinmkt_parse_and_deeplink, gecko_parse_and_deeplink)]
    print(deeplink_list)
    print(len(deeplink_list))



