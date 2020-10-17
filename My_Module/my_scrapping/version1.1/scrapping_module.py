import numpy as np
import os, requests, time
from time_countdown import workload_time_left as lte
from selenium import webdriver


class Scrapping():

    def __init__(self, url, folder_names, file_names, method = 'requests', sleep_mode = 'Default'):
        self.headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
        self.path = os.getcwd()
        self.url_list = url
        self.folder_names = folder_names
        self.file_list = file_names
        self.file_path = None
        self.url_index = None
        self.file_name = None
        self.total_workload = None
        self.workload = None
        self.url = None
        self.start_time = None
        self.end_time = None
        self.sleep = None
        self.method = method
        self.sleep_mode = sleep_mode


    def folder_setup(self):
        '''
        Check if the folder to store html is existed. If not create
        a new folder named by your setting, i.e., <folder_name>.
        Then initialize scrapping process, i.e., check html file existence.
        '''

        self.path = os.path.join(self.path, self.folder_names)
        if not os.path.exists(self.path):
            os.mkdir(self.path)
        else:
            print('\nDirectory' + self.format_output(self.folder_names) +\
                    'already exists!\n')

        self.check_file_exists()


    def check_file_exists(self):
        '''
        Check whether the target html file exists. If not, start 
        scrapping process, otherwise process to next url.
        '''
        
        self.workload = len(self.url_list)
        self.total_workload = len(self.url_list)

        for url in self.url_list:
            # start counting time of this round.
            self.start_time = time.time()
            # this arg will be used when calling requests.get()
            self.url = url
            self.url_index = self.url_list.index(url)
            # Start from 1, showing scrapping process, i.e., (1/10)
            self.work_count = self.url_index + 1
            # Page1.html
            self.file_name = self.file_list[self.url_index] + '.html'
            # Absolute file path
            self.file_path = os.path.join(self.path, self.file_name)

            if not os.path.exists(self.file_path):
                self.start_scrapping()

            else:
                self.workload -= 1
                print('\nFile' + self.format_output(self.file_name) +\
                        'alrady exists!')
        
        print('\nDone! You have finished this section!')



    def start_scrapping(self):
        '''
        Download webpage and save as html file in your folder.
        Return time estimation for finishing downloading all URLs.
        '''

        print('\nScrapping' + self.format_output(self.file_name) + \
                '...'*13 + '(%d/%d)' % (self.work_count, self.total_workload))


        #if self.method == 'requests':
        #    r = requests.get(self.url, headers = self.headers)
        #    html = r.text

        #elif self.method == 'selenium':
        #    driver = webdriver.Chrome()
        #    driver.get(self.url)
        #    html = driver.page_source
        #    driver.close()


        #self.file_setup(html)
        self.workload -= 1
        print('Finish downloading [ %s ]...' % self.file_name)

        self.end_time = time.time()
        round_time = self.end_time - self.start_time

        if self.workload != 0:
            if self.sleep_mode == 'Default':
                self.sleep = np.random.randint(5,10) + np.random.normal(8,3)
                print('Program sleeps for' + self.format_output(self.sleep) + \
                'seconds...')
                lte(round_time, self.sleep, self.workload)
                print('\n')
                time.sleep(self.sleep)
            else:
                self.sleep = self.sleep_mode
                print('Program sleeps for' + self.format_output(self.sleep) + \
                'seconds...')
                lte(round_time, self.sleep, self.workload)
                print('\n')
                time.sleep(self.sleep)
        

    def file_setup(self, html):
        '''
        Save sources code into your local html file.
        '''

        with open(self.file_path + 'temp', 'w', encoding = 'utf-8') as f:
            f.write(html)
        os.rename(self.file_path + 'temp', self.file_path)


    def format_output(self, output):
        '''
        Format printing output in same form, i.e., [ output ]
        '''

        result = ' [ ' + str(output) + ' ] '

        return result




if __name__ == '__main__':
    url_base = 'https://coinmarketcap.com/'
    url = [url_base + str(i) + '/' for i in range(5)]
    folder_name = 'html_file'
    file_names = ['Page' + str(i) for i in range(len(url))]
    Scrapping(url, folder_name, file_names, sleep_mode = 5).folder_setup()



