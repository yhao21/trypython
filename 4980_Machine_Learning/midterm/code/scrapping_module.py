import numpy as np
import os, requests, time, glob, re, datetime
from time_countdown import workload_time_left as lte



class Scrapping():

    def __init__(self, url_list, folder_name, hours):
        self.url_list = url_list
        self.folder_name = folder_name
        # code path, home dir
        self.root = os.getcwd()
        self.folder_path = []
        self.workload = None
        self.file_name_base = None
        self.total_hours = hours
        self.count = 1
        self.web_name = None
        self.repeat_times = None
        self.url = None
        self.headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
        self.work_leftover = None
        self.finish_file = []
        self.no_page_sleep = False
        self.no_repetition_sleep = False
        


    def folder_setup(self):
        '''
        Check the existence for folders to store html files.
        If not, create one.
        Otherwise, print existence
        '''

        for name in self.folder_name:

            folder_path = os.path.join(self.root, name)

            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            else:
                print('\nDirectory' + self.output_format(name) + \
                        'already exists! \n')

            self.folder_path.append(folder_path)


        # gather all existing files for later checking process.
        # if folder is not empty, gather all existing files for later checking process.
        if os.listdir(self.folder_path[0]):
            for coinfile in glob.glob(os.path.join(self.folder_path[0], '*.html')):
                name_for_check = re.compile(r'.*\d*_15.*page\d*').findall(coinfile)[0]
                self.finish_file.append(name_for_check)

        if os.listdir(self.folder_path[1]):
            for geckofile in glob.glob(os.path.join(self.folder_path[1],'*.html')):
                name_for_check = re.compile(r'.*\d*_15.*page\d*').findall(geckofile)[0]
                self.finish_file.append(name_for_check)

        self.check_file_existence()


    def remove_tempfile(self):
        '''
        Remove all temp files when you restart the program
        '''
        
        for folder in self.folder_path:
            for rmfile in glob.glob(folder + '/*.temp'):
                os.remove(rmfile)

    
    

    def check_file_existence(self):
        '''
        Check the existence of target html file.
        If not, start scrapping process.
        Otherwise, print feedback, process to next url
        '''

        self.remove_tempfile()

        self.repeat_times = self.repeats()
        website = ['coinmkt', 'gecko']

        while self.count < self.repeat_times + 1:

            self.workload = len(self.url_list)
            self.work_leftover = len(self.url_list)

            # a pair of url for the nth page
            # url_order = (coin_url, gecko_url)
            for url_order in self.url_list:
    
                # web_url is a url for either coin or gecko
                # web_url = coin_url, web_url = gecko_url
                # the for loop below do the preparation of a particular page
                # from both coinmkt and gecko.
                for web_url in url_order:
    
                    # get page number
                    order = re.compile('(\d)').findall(web_url)[0]
                    self.file_name_base = 'page' + str(order)
                    t_stamp = datetime.datetime.fromtimestamp(time.time()).strftime('%m-%d-%H-%M-%S')
    
                    # file name:
                    # 4_15_page5_10-19-21-33-29
                    self.file_name = str(self.count) + '_15_' + self.file_name_base + '_' + t_stamp

                    # remember self.folder_path is a list, first element is coin's, second for gecko.
                    # url_order also have two element, first is coin's url, second for gecko's
                    # which_web gets the index(0 or 1), hence, we can find trace folder path for each web.
                    # file_path: /home/synferlo/git/trypython/4980_Machine_Learning/midterm/code/gecko_html_file/4_15_page5_10-19-21-39-11.html
                    which_web = url_order.index(web_url)
                    self.web_name = website[which_web]
                    self.file_path = os.path.join(self.folder_path[which_web], self.file_name + '.html')
                    self.url = web_url

                    # i.e., 1_15_page1
                    check_file_name = re.compile(r'.*page\d*').findall(self.file_name)[0]
                    # i.e., /home/synferlo/git/trypython/4980_Machine_Learning/midterm/code/coinmktcap_html_file/1_15_page2
                    check_file_path = os.path.join(self.folder_path[which_web], check_file_name)

                    if check_file_path not in self.finish_file:
                        self.start_scrapping()
                    else:
                        print('\nFile' + self.output_format(website[which_web] + ': ' + check_file_name) + 'already exists!')
                        self.no_page_sleep = True
                        self.no_repetition_sleep = True

                # how many pages need to download. page range is in [1,5]
                # after download each page, workload - 1, i.e., 4,3,2,1,0
                # need to sleep after downloading webpage except the 5th page in each repeat_time
                self.work_leftover -= 1
                if not self.work_leftover == 0:
                    # test
                    #sleep_time = 1
                    # if file exists you don't want to sleep
                    if not self.no_page_sleep:
                        sleep_time = self.sleep_time()
                        print('\nProgram sleeps for' + self.output_format(sleep_time) + 'seconds...')
                        print('-' * 100 + '\n\n')
                        time.sleep(sleep_time)
                    self.no_page_sleep = False
        
            
            print(self.finish_repeats() + '\n    ----> Sleep for 15 mins...')
            print('-' * 100 + '\n\n')
            self.count += 1
            # test
            if not self.no_repetition_sleep:
                time.sleep(15 * 60)
            self.no_repetition_sleep = False


        print('\nDone! You have downloaded %s hour(s) data!' % self.output_format(self.total_hours))
    


    def start_scrapping(self):
        '''
        scrape html source code from both website
        '''

        # print scrapping process, format: <nth 15 mins>/<how many 15 mins in total>
        # i.e., for a 1 hour's program, there are 4 15-mins, (1/4), (2/4), (3/4), (4/4), Done.
        print('\nScrapping' + self.output_format(self.web_name + ': ' + self.file_name_base) \
                + '...' * 20 + '(%d/%d)' % (self.count, self.repeat_times))

        # test
        #r = requests.get(self.url, headers = self.headers)
        #html = r.text
        #self.save_html_file(html)
        print(' ' * 4 + '----> Finish...')


    def save_html_file(self, content):
        '''
        save source code to a html file
        '''

        with open(self.file_path + '.temp', 'w', encoding = 'utf-8') as f:
            f.write(content)
        os.rename(self.file_path + '.temp', self.file_path)



    def sleep_time(self):
        '''
        Generate a sleep time
        '''

        return np.random.randint(5,10) + np.random.normal(8,3)



    def output_format(self, item):
        '''
        format output need to print
        '''
        return ' [ ' + str(item) + ' ] '



    def repeats(self):
        '''
        compute how many 15 mins in self_total_hours
        '''

        return self.total_hours*4



    def finish_repeats(self):
        '''
        Feedback after each 15-mins round
        '''

        if self.count == 1:
            order = 'st'
        elif self.count == 2:
            order = 'nd'
        elif self.count == 3:
            order = 'rd'
        else:
            order = 'th'

        return '\nFinish downloading the' + self.output_format(str(self.count) + str(order)) + "15-min data" 




if __name__ == '__main__':

    url_coin_base = 'https://coinmarketcap.com/' 
    url_gecko_base = 'https://www.coingecko.com/en?page=' 
    url_list = [(url_coin_base + str(i), url_gecko_base + str(i)) for i in range(1,6)]
    folder_name = ['coinmktcap_html_file', 'gecko_html_file']
    Scrapping(url_list, folder_name, 1).folder_setup()























