import requests, os, time
import numpy as np





class data_scrappying():
    def __init__(self, file_folder, file_name, url):
        self.file_folder = file_folder
        self.file_name = file_name
        self.url = url
        self.headers = {'user-agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}




    def check_file_existence(self):
        self.filepath = os.path.join(self.file_folder, self.file_name)
        if not os.path.exists(self.filepath):
            self.start_scrappying()
        else:
            print(f'File {self.file_name} exists!')

    def file_setup(self, content):
        with open(f'{self.filepath}.temp', 'w', encoding = 'utf-8') as f:
            f.write(content)
        os.rename(f'{self.filepath}.temp', self.filepath)


    def start_scrappying(self):
        r = requests.get(self.url, headers = self.headers)
        html = r.text
        self.file_setup(html)

        sleeptime = np.random.randint(3,5) + np.random.normal(5,3)
        if sleeptime < 0:
            sleeptime = -sleeptime
        print(f'Finish [{self.file_name}], sleep: {sleeptime}')
        time.sleep(sleeptime)







if __name__ == '__main__':

    page_range = [1,97]
    file_folder = 'html_dir'
    if not os.path.exists(file_folder):
        os.mkdir(file_folder)

    for page in range(page_range[0], page_range[1]):
        file_name = f'page_{page}.html'
        # homepage url (coinmarketcap)
        #url = f'https://coinmarketcap.com/?page={page}/'
        # coingecko
        url = f'https://www.coingecko.com/en?page={page}'

        data_scrappying(file_folder, file_name, url).check_file_existence()
    
