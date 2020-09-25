import requests, os, time
import time_countdown as cd
from selenium import webdriver


class Scrapping():
    """
    url is a list of all urls
    file_name is a list of file_names

    submit the upper two parameters and the folder name to Scrapping
    then, this module will download the page(s) for you. and save html files in the folder you named.
    """
    def __init__(self, ui, progress):
        self.headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'}
        self.url_list = None
        self.url = ''
        self.file_name = None
        self.folder_name = None
        self.path = os.getcwd()
        self.html = 0
        self.page_count = 0
        self.file_index = 0
        self.file_path = ''
        self.st = None
        self.et = None
        self.method = None
        self.spage = None
        self.epage = None
        self.full_url = None
        self.front_url = None
        self.rear_url = None
        self.page_rule = None
        self.ui = ui
        self.pb = progress


    def init_machine(self, method, url_mode, folder_name, start_page = 0, end_page = 0, file_name = None, full_url = '', front_url = '', rear_url = '', page_rule = ''):
        self.method = method
        self.folder_name = folder_name

        if url_mode == 'Single Page':
            self.file_name = [file_name]
            self.full_url = full_url
            self.one_part_url()

        if url_mode == 'Multi Pages':

            self.front_url = front_url
            self.rear_url = rear_url
            self.spage = int(start_page)
            self.epage = int(end_page)
            self.file_name = ['page' + str(i) for i in range(self.spage, self.epage + 1)]
            self.page_rule = page_rule
            self.n_part_url()


    def one_part_url(self):
        self.url_list = [self.full_url]
        self.folder_setup()
        self.finish()


    def n_part_url(self):
        if self.page_rule == '1,2,3,...':
            self.url_list = [self.front_url + str(page) + self.rear_url for page in range(self.spage, self.epage + 1)]
        if self.page_rule == '0,50,100,...':
            self.url_list = [self.front_url + str((page - 1) * 50) for page in range(self.spage, self.epage + 1)]
        if self.page_rule == '0,5,10,...':
            self.url_list = [self.front_url + str((page - 1) * 5) for page in range(self.spage, self.epage + 1)]

        self.folder_setup()
        self.finish()


    def folder_setup(self):
        self.path = self.folder_name
        if not os.path.exists(self.path):
            os.mkdir(self.path)

        self.check_file_exists()

    # def folder_setup(self):
    #     self.path = os.path.join(self.path, self.folder_name)
    #     if not os.path.exists(self.path):
    #         os.mkdir(self.path)
    #
    #     self.check_file_exists()


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
                info = '\n[' +self.file_name[self.file_index] + ']' + 'has already existed.......' + '%s/%s' % (str(len(self.url_list) - self.page_count), len(self.url_list))
                self.ui.console.clear()
                self.ui.console.addItem(info)

                print('\n[' +self.file_name[self.file_index] + ']' + 'has already existed.......' + '%s/%s' % (str(len(self.url_list) - self.page_count), len(self.url_list)))


    def file_setup(self):
        with open(self.file_path + '.temp', 'w', encoding = 'utf-8') as f:
            f.write(self.html)
        os.rename(self.file_path + '.temp', self.file_path+ '.html')
        try:
            os.remove(self.file_path + '.temp')
        except:
            pass


    def scrapping(self):
        if self.method == 'Requests':
            r = requests.get(self.url, headers = self.headers)
            self.html = r.text

        if self.method == 'Selenium':
            driver = webdriver.Chrome()
            driver.get(self.url)
            self.html = driver.page_source
            driver.close()


        self.file_setup()
        sleep = 2
        time.sleep(sleep)
        self.page_count -=1
        info = '\nFinish downloading [' + self.file_name[self.file_index] + ']'+ '.......' + '%s/%s' % (str(len(self.url_list) - self.page_count), len(self.url_list))
        self.ui.console.clear()
        self.ui.console.addItem(info)

        print('\nFinish downloading [' + self.file_name[self.file_index] + ']'+ '.......' + '%s/%s' % (str(len(self.url_list) - self.page_count), len(self.url_list)))
        # round_end time
        self.et = time.time()
        round_time = self.et - self.st
        time_left = cd.left_time_estimation(round_time, sleep, self.page_count)
        self.ui.console.addItem(time_left)


    def finish(self):
        self.ui.console.addItem('\nMission Completed!')
        return False



if __name__ == '__main__':
    base_url = 'https://coinmarketcap.com/rankings/exchanges/'
    url = [base_url + str(i) + '/' for i in range(1,6)]
    folder_name = 'main page'
    file_name = ['page ' + str(i) for i in range(1, len(url) + 1)]
    # Scrapping(url, file_name, folder_name).folder_setup()


