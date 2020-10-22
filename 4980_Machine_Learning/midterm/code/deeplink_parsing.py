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


    def init_file(self):
        '''
        Locate html folder to parse.
        '''

        # /home/synferlo/git/trypython/4980_Machine_Learning/midterm/code/coin_500deeplink
        self.file_path = os.path.join(self.path, self.folder)


    def parsing_deeplink(self):
        '''
        Parsing more detail info for each crypto currency.
        '''

        self.init_file()

        total_workload = len(glob.glob(self.file_path + '/*.html'))
        workload = len(glob.glob(self.file_path + '/*.html'))

        one_file = glob.glob(self.file_path + '/*.html')[1]

        with open(one_file, 'r') as f:
            html = f.read()

        soup = BeautifulSoup(html, 'html.parser')
        rows = soup.find('tbody', {'class':'cmc-details-panel-about__table'}).find_all('tr')
        
        ######################
        ###add coin name!#####
        ######################
        name = re.compile(r'(.*) Price').findall(rows[0].find('strong').string)[0]
        #mktcap_rank = rows[2].find('td').string.replace('#', '')
        #cir_supply = self.remove_coin_name(rows[5].find('td').string).replace(',', '')
        #max_supply = self.remove_coin_name(rows[7].find('td').string).replace(',', '')
        #all_time_high = self.remove_coin_name(rows[8].find('td').find('div').string).replace('$','').replace(',', '')
        #all_time_low = self.remove_coin_name(rows[9].find('td').find('div').string).replace('$','').replace(',', '')
        #print(name)


    def remove_coin_name(self, info_input):
        '''
        Remove currency name after numerical value.
        '''

        return re.compile(r'(.*) \w*').findall(info_input)[0]
        












        


if __name__ == "__main__":
    folder = 'coin_500deeplink'
    ParsingDeepLink(folder).parsing_deeplink()
















