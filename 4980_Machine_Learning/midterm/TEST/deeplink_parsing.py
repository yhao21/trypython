import os, glob, re, time
import pandas as pd
from bs4 import BeautifulSoup
from time_countdown import workload_time_left as wtl




class ParsingDeepLink():

    def __init__(self, html_folder):
        self.path = os.getcwd()
        self.folder = html_folder
        self.df = pd.DataFrame()
        self.file_path = None
        self.error_df = None
        self.log_name = 'Error_Log'
        self.fname = None
        self.coin_df_name = 'Coin_500Deeplink_Info.csv'
        self.gecko_df_name = 'Gecko_500Deeplink_Info.csv'


    def init_file(self):
        '''
        Locate html folder to parse.
        '''

        # /home/synferlo/git/trypython/4980_Machine_Learning/midterm/code/coin_500deeplink
        self.file_path = os.path.join(self.path, self.folder)



    def parsing_coin_deeplink(self):
        '''
        Parsing more detail info for each crypto currency.
        '''

        # remove error log when you restart this program.
        if os.path.exists(self.log_name + '.csv'):
            os.remove(self.log_name + '.csv')

        self.init_file()

        total_workload = len(glob.glob(self.file_path + '/*.html'))
        workload = len(glob.glob(self.file_path + '/*.html'))

        ### test
        #for one_file in glob.glob(self.file_path + '/polkadot-new.html'):
        for one_file in glob.glob(self.file_path + '/*.html'):

            start_time = time.time()
            # fname is saved for pair url if error occur during the parsing process.
            # i.e., ethereum
            self.fname = re.compile(r'link/(.*).html').findall(one_file)[0]
            

            with open(one_file, 'r') as f:
                html = f.read()

            soup = BeautifulSoup(html, 'html.parser')
            rows = soup.find('tbody', {'class':'cmc-details-panel-about__table'}).find_all('tr')
            
            # it is also the file_name
            coin_name = re.compile(r'(.*) Price').findall(rows[0].find('strong').string)[0].replace(' ','').lower()
            table_header = soup.find('div',\
                    {'class':'v5fhlm-0 jdAFKL cmc-details-panel-tabs col-xs-12'}).\
                    find('ul',{'class':'cmc-tabs__header'}).find_all('li')
            # /currencies/bytom/ratings/
            rating_base = table_header[5].find('a')['href']
            rating_url = 'https://coinmarketcap.com/' + rating_base

            try:
                # delete all space, and trans to lower case, because sometimes, names in both
                # webs are different.
                mktcap_rank = rows[2].find('td').string.replace('#', '')
                cir_supply = self.remove_coin_name(rows[5].find('td').string).replace(',', '')
                all_time_high = self.remove_coin_name(rows[8].find('td').find('div').string).replace('$','').replace(',', '')
                all_time_low = self.remove_coin_name(rows[9].find('td').find('div').string).replace('$','').replace(',', '')

                # [<div>$0.065951 USD /</div>, <div>$0.060618 USD</div>]
                days_7_high_low = rows[13].find('td').find_all('div')
                days_7_high = days_7_high_low[0].string.replace('$', '').replace\
                        ('USD /', '')
                days_7_low = self.remove_coin_name(days_7_high_low[1].string).\
                        replace('$','')

                self.df = self.df.append({
                    'name':coin_name,
                    'rank':mktcap_rank,
                    'circulating_supply':cir_supply,
                    'all_time_high':all_time_high,
                    'all_time_low':all_time_low,
                    '7_days_high':days_7_high,
                    '7_days_low':days_7_low,
                    'rating_url':rating_url
                    },ignore_index = True)

            except:
                try:
                    # these coinmkt web, has four side panels, info are in different 
                    tables = soup.find_all('tbody',{'class':'cmc-details-panel-about__table'})
                    rank = tables[0].find_all('tr')[4].find('td').string.replace('#', '')
                    cir_supply = re.compile(r'(.*) \w*').findall(tables[-1].find_all('tr')[0].find('td').string)[0].replace(',','')
                    all_time_high = re.compile(r'\$(.*) \w*').findall(tables[2].find_all('tr')[4].find('td').find('div').string)[0]
                    all_time_low = re.compile(r'\$(.*) \w*').findall(tables[2].find_all('tr')[5].find('td').find('div').string)[0]
                    days_7_high = re.compile(r'\$(.*) \w* \/').findall(tables[2].find_all('tr')[0].find('td').find('div').string)[0]
                    days_7_low = re.compile(r'\$(.*) \w*').findall(tables[2].find_all('tr')[0].find('td').find_all('div')[1].string)[0]
                    print(all_time_high)
                    print(all_time_low)
                    print(days_7_high)
                    print(days_7_low)

                    self.df = self.df.append({
                        'name':coin_name,
                        'rank':mktcap_rank,
                        'circulating_supply':cir_supply,
                        'all_time_high':all_time_high,
                        'all_time_low':all_time_low,
                        '7_days_high':days_7_high,
                        '7_days_low':days_7_low,
                        'rating_url':rating_url
                        },ignore_index = True)

                except:

                    print('\nERROR:')
                    print('Website does contain full info about this currency')
                    print('Info of this error is saved to' + self.output_format(self.log_name))
                    # you should add name and deeplinks(url) to df even if other detail info can't be parsed.
                    # otherwise, you cannot pair gecko's url with coin's url, i.e., 20 coin_url and 19 gecko_url
                    self.df = self.df.append({
                        'name':coin_name,
                        'rating_url':rating_url,
                        }, ignore_index = True)
                    self.save_to_log()

            workload -= 1
            nth_file = total_workload - workload
            round_time = time.time() - start_time
            print('\nFinish parsing' + self.output_format(self.fname) + \
                    '...' * 20 + '(%d/%d)' % (nth_file, total_workload))
            wtl(round_time, 0, workload)
            print('-' * 100 + '\n\n')


        order = ['name','rank','circulating_supply', 'all_time_high', 'all_time_low', '7_days_high', '7_days_low', 'rating_url']
        self.df = self.df[order]
        self.df.to_csv(self.coin_df_name)
        print(self.df)




    def parsing_gecko_deeplink(self):
        '''
        Parsing more detail info for each crypto currency.
        '''

        self.init_file()
        self.deeplink_dataframe = pd.read_csv('500deeplinks.csv')

        total_workload = len(glob.glob(self.file_path + '/*.html'))
        workload = len(glob.glob(self.file_path + '/*.html'))

        for one_file in glob.glob(self.file_path + '/*.html'):

            start_time = time.time()
            # fname is saved for pair url if error occur during the parsing process.
            # i.e., ethereum
            self.fname = re.compile(r'link/(.*).html').findall(one_file)[0]

            # return df like this:  https://www.coingecko.com/en/coins/arpa-chain  arpa-chain
            #                       https://coinmarketcap.com/currencies/medibloc  medibloc
            # Use str.contains to extract rows for gecko. We don't need coinmktcap's info here.
            self.url_base = self.deeplink_dataframe.loc[self.deeplink_dataframe['name'] == self.fname]
            self.url_base = self.url_base.loc[self.url_base['deeplinks'].str.contains('www.coingecko.com')]
            # [unname, name, deeplinks]
            self.url_base = self.url_base.iloc[:, 2].values[0]

            with open(one_file, 'r') as f:
                html = f.read()


            name = re.compile(r'<th scope="row" class="border-top-0"><strong>(.*?) Price</strong></th>').findall(html)[0].lower().replace(' ','')
            rank = re.compile(r'<th scope="row">Market Cap Rank</th>\n<td>\n#(.*?)\n</td>').findall(html)[0]
            ROI = str(re.compile(r'ROI').findall(html))

            soup = BeautifulSoup(html, 'html.parser')
            rows = soup.find('div',{'class':'col-lg-4 card-column d-flex flex-column-reverse flex-sm-column order-3 order-sm-3 order-md-3 order-lg-2'}).find('table').find_all('tr')

            table_header = soup.find('div',{'class':'tab-content'}).find('ul').find_all('li')
            rating_base = table_header[6].find('a')['href']
            rating_url = self.url_base + rating_base

            try:
                # some page has ROI in the panel, this may change the order of all other tds
                if ROI == "['ROI']":
                    days_7_high_low = rows[7].find('td').find_all('span')
                    days_7_low = days_7_high_low[0].string.replace('$','').replace(',','')
                    days_7_high = days_7_high_low[1].string.replace('$','').replace(',','')
                    all_time_high =rows[9].find('td').find('span').string.replace('$','').replace(',','')
                    all_time_low = rows[10].find('td').find('span').string.replace('$','').replace(',','')
                else:
                    days_7_high_low = rows[6].find('td').find_all('span')
                    days_7_low = days_7_high_low[0].string.replace('$','').replace(',','')
                    days_7_high = days_7_high_low[1].string.replace('$','').replace(',','')
                    all_time_high = rows[8].find('td').find('span').string.replace('$','').replace(',','')
                    all_time_low = rows[9].find('td').find('span').string.replace('$','').replace(',','')

                self.df = self.df.append({
                    'name':name,
                    'rank':rank,
                    'all_time_high':all_time_high,
                    'all_time_low':all_time_low,
                    '7_days_high':days_7_high,
                    '7_days_low':days_7_low,
                    'rating_url':rating_url,
                    },ignore_index = True)

            except:
                print('\nERROR:')
                print('Website does contain full info about this currency')
                print('Info of this error is saved to' + self.output_format(self.log_name))

                # you should add name and deeplinks(url) to df even if other detail info can't be parsed.
                # otherwise, you cannot pair gecko's url with coin's url, i.e., 20 coin_url and 19 gecko_url
                self.df = self.df.append({
                    'name':name,
                    'rating_url':rating_url,
                    }, ignore_index = True)
                self.save_to_log()

            workload -= 1
            nth_file = total_workload - workload
            round_time = time.time() - start_time
            print('\nFinish parsing' + self.output_format(self.fname) + \
                    '...' * 20 + '(%d/%d)' % (nth_file, total_workload))
            wtl(round_time, 0, workload)
            print('-' * 100 + '\n\n')


        order = ['name','rank', 'all_time_high', 'all_time_low', '7_days_high', '7_days_low', 'rating_url']
        self.df = self.df[order]
        self.df.to_csv(self.gecko_df_name)
        print(self.df)



    def save_to_log(self):
        '''
        Save fname and url for those pages missing detail data.
        Users can re-download these data manually.
        '''
        #print(df.loc[df['Severity'] == 3])

        df = pd.read_csv('500deeplinks.csv')
        missing_coin = df.loc[df['name'] == self.fname].values
        # missing_coin is a list contain elements, each is a list.
        # first element is coinmktcap's info, the 2nd element of coinmkt's list
        # is url info for this cryptocurrency
        #[[2 'ethereum' 'https://coinmarketcap.com/currencies/ethereum' ]
        #[3 'ethereum' 'https://www.coingecko.com/en/coins/ethereum' ]] 
        url = missing_coin[0][2]

        if not os.path.exists(self.log_name + '.csv'):
            self.error_df = pd.DataFrame()
        else:
            self.error_df = pd.read_csv(self.log_name + '.csv')

        self.error_df = self.error_df.append({
            'name':self.fname,
            'deeplinks':url
            }, ignore_index = True)

        order = ['name', 'deeplinks']
        self.error_df = self.error_df[order]
        self.error_df.to_csv(self.log_name + '.csv')





    def remove_coin_name(self, info_input):
        '''
        Remove currency name after numerical value.
        '''

        return re.compile(r'(.*) \w*').findall(info_input)[0]
        


    def output_format(self, item):
        '''
        format output need to print
        '''
        return ' [ ' + str(item) + ' ] '




    def parsing_coin_rating(self):

        self.init_file()

        total_workload = len(glob.glob(self.file_path + '/*.html'))
        workload = len(glob.glob(self.file_path + '/*.html'))

        one_file = glob.glob(self.file_path + '/bitcoin.html')[0]
        
        with open(one_file, 'r') as f:
            html = f.read()
        
        soup = BeautifulSoup(html, 'html.parser')
        a = soup.find('div', {'id':'js-fcas-spectrum'}).findall('div')
        print(a)
        #for one_file in glob.glob(self.file_path + '/*.html'):
        #    fname = re.compile(r'rating_html/(.*).html').findall(one_file)[0]


            #start_time = time.time()
            ## fname is saved for pair url if error occur during the parsing process.
            ## i.e., ethereum
            #self.fname = re.compile(r'link/(.*).html').findall(one_file)[0]
            #

            #with open(one_file, 'r') as f:
            #    html = f.read()




        


if __name__ == "__main__":

    #folder = 'coin_rating_html'
    #ParsingDeepLink(folder).parsing_coin_rating()





    '''
    !!! Call different parsing functions with [different folder names]!!
    '''
    #folder = 'coin_500deeplink'
    #ParsingDeepLink(folder).parsing_coin_deeplink()
    #folder = 'gecko_500deeplink'
    #ParsingDeepLink(folder).parsing_gecko_deeplink()
















