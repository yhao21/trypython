import requests, os, time
import time_countdown as cd
from selenium import webdriver


class Scrapping():
    """
    url is a list of all url
    file_name is a list of file_name

    submit the upper two parameters and the folder name to Scrapping
    then, this module will download the page(s) for you. and save html files in the folder you named.
    """
    def __init__(self, url, file_name, folder_name, method = 'requests'):
        self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        self.url_list = url
        self.url = ''
        self.file_name = file_name
        self.folder_name = folder_name
        self.path = os.getcwd()
        self.html = 0
        self.page_count = 0
        self.file_index = 0
        self.file_path = ''
        self.st = None
        self.et = None
        self.method = method


    def folder_setup(self):
        self.path = os.path.join(self.path, self.folder_name)
        if not os.path.exists(self.path):
            os.mkdir(self.path)

        self.check_file_exists()


    def check_file_exists(self):
        self.page_count = len(self.url_list)
        for url in self.url_list:
            # round_start time
            self.st = time.time()

            self.url = url
            self.file_index = self.url_list.index(url)
            self.file_path = os.path.join(self.path, self.file_name[self.file_index])

            if not os.path.exists(self.file_path + '.html'):
                self.scrapping()
            else:
                self.page_count -= 1
                print('\n[' +self.file_name[self.file_index] + ']' + 'has already existed.......' + '%s/%s' % (str(len(self.url_list) - self.page_count), len(self.url_list)))


    def file_setup(self):
        with open(self.file_path + '.temp', 'w', encoding = 'utf-8') as f:
            f.write(self.html)
        os.rename(self.file_path + '.temp', self.file_path+ '.html')


    def scrapping(self):
        if self.method == 'requests':
            r = requests.get(self.url, headers = self.headers)
            self.html = r.text

        if self.method == 'selenium':
            driver = webdriver.Chrome()
            driver.get(self.url)
            self.html = driver.page_source
            driver.close()

        self.file_setup()
        sleep = 2
        time.sleep(sleep)
        self.page_count -=1
        print('\nFinish downloading [' + self.file_name[self.file_index] + ']'+ '.......' + '%s/%s' % (str(len(self.url_list) - self.page_count), len(self.url_list)))
        # round_end time
        self.et = time.time()
        round_time = self.et - self.st
        cd.left_time_estimation(round_time, sleep, self.page_count)



if __name__ == '__main__':
    base_url = 'https://coinmarketcap.com/rankings/exchanges/'
    url = [base_url + str(i) + '/' for i in range(1,6)]
    folder_name = 'main page'
    file_name = ['page ' + str(i) for i in range(1, len(url) + 1)]
    Scrapping(url, file_name, folder_name, 'selenium').folder_setup()

