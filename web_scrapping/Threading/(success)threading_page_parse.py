import threading
import os
import time
from bs4 import BeautifulSoup
import glob
import re
from queue import Queue
import pandas as pd

Parse_Exit = False


class page_parsing(threading.Thread):
    def __init__(self,parser,file_queue):
        super().__init__()
        self.parser = parser
        self.file_queue = file_queue
    def run(self):
        while not Parse_Exit:
            try:
                df = pd.DataFrame()
                file_name = self.file_queue.get(False)
                csv_name = re.compile(r'.*?\\(.*)\.html').findall(file_name)
                if not os.path.exists("coinmarketcap_html_file/" + str(csv_name) + ".csv"):
                    f = open(file_name,'r',encoding="utf-8")
                    content = f.read()
                    soup = BeautifulSoup(content,"html.parser")
                    items = soup.find('tbody').find_all('tr')
                    for item in items:
                        tds = item.find_all('td')
                        name = tds[1].text
                        mkt_cap = tds[2].text
                        price = tds[3].text
                        volume_24hrs = tds[4].text
                        cir_sup = tds[5].text
                        change = tds[6].text
                        df = df.append({
                            '1.Name':name,
                            '2.Market Cap':mkt_cap,
                            '3.Price':price,
                            '4.Volume(24h)':volume_24hrs,
                            '5.Circulating Supply':cir_sup,
                            '6.Change':change
                        },ignore_index = True)
                    csv_name = re.compile(r'.*?\\(.*)\.html').findall(file_name)
                    df.to_csv("coinmarketcap_html_file/" + str(csv_name) + ".csv.temp")
                    os.rename("coinmarketcap_html_file/" + str(csv_name) + ".csv.temp","coinmarketcap_html_file/" + str(csv_name) + ".csv")
                    print("finish parsing " + file_name)
                else:
                    print('file exist')
            except:
                pass

def main():
    ##因为filename是通过glob路径存储的，所以在执行f = open时打开的一定是对应路径的文件，保存csv时也是用filename确保数据与文件匹配
    files = glob.glob('coinmarketcap_html_file/*.html')
    file_queue = Queue()
    for file in files:
        file_queue.put(file)

    parser_list = ['parser1','parser2','parser3','parser4','parser5']
    thread_parser = []

    for parser in parser_list:
        thread = page_parsing(parser,file_queue)
        thread.start()
        thread_parser.append(thread)

    while not file_queue.empty():
        pass
    global Parse_Exit
    Parse_Exit = True

    for thread in thread_parser:
        thread.join()
    total_time = time.time() - start_time
    print('Finish in (seconds) :',total_time)

if __name__=="__main__":
    start_time = time.time()
    main()