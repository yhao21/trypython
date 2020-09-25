import requests, os, re
from selenium import webdriver




class Scrapping():

    def __init__(self, file_path, s_mode):
        self.mode = s_mode
        self.f_path = file_path



    def mode_selection(self):
        self.url = input('url: ')
        self.name = input('file_name:')

        if self.mode == 'r':
            self.requests_scrapping()
        if self.mode == 's':
            self.selenium_scrapping()


    def requests_scrapping(self):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}
        url = self.url
        r = requests.get(url, headers = headers)
        html = r.text

        with open(os.path.join(self.f_path, self.name) + '.html', 'w', encoding = 'utf-8') as f:
            f.write(html)

        print('Finish downloading ' + self.name)


    def selenium_scrapping(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        html = driver.page_source
        driver.close()
        with open(os.path.join(self.f_path, self.name) + '.html', 'w', encoding = 'utf-8') as f:
            f.write(html)

        print('finish downloading ' + self.name)


if __name__ == '__main__':
    pass






