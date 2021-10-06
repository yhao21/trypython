import requests
import time
import datetime
import os
from queue import Queue
import threading
import re
import glob

Requests_Exit = False

class page_download(threading.Thread):
    def __init__(self,spider,page_queue):
        super().__init__()
        self.spider = spider
        self.page_queue = page_queue
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

    #为什么名字不是run就无法运行

    def run(self):
        while not Requests_Exit:
            try:
                page_number = self.page_queue.get(False)
                """
                当文件名中加入下载时的timestamp时，目前没找到通过os直接查找文件名的方法
                故，只能通过glob和re检查整个文件夹内部是否存在带有该页码的文件，
                """
                files = glob.glob('ebay_laptop_html_file/*.html')
                if not str(re.compile(r'.*?\\page # ' + str(page_number) + '__time-(.*?)\.html').findall(str(files))) != '[]':
                    url = 'https://www.ebay.com/sch/i.html?_from=R40&_nkw=laptop&_sacat=0&_pgn=' + str(page_number)
                    currenttime = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S')
                    f = open('ebay_laptop_html_file/page # ' + str(page_number) + '__time-' + currenttime + '.html.temp','w',encoding='utf-8')
                    r = requests.get(url,headers = self.headers)
                    r.encoding = r.apparent_encoding
                    html = r.text
                    f.write(html)
                    f.close()
                    os.rename('ebay_laptop_html_file/page # ' + str(page_number) + '__time-' + currenttime + '.html.temp','ebay_laptop_html_file/page # ' + str(page_number) + '__time-' + currenttime + '.html')
                    print('finish downloading: page #' + str(page_number) + '__time-' + currenttime +'.html')
                    #打印现在时间目的：在自己电脑上长时间爬数据后，根据时间间隔和上一次下载成功时间判断有多少时间可以用来关机修整电脑
                    print('current time:' + datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d-%H-%M-%S'))
                else:
                    print('file: ' + 'page # ' + str(page_number) + 'exist')
            except:
                pass

def main():
    if not os.path.exists('ebay_laptop_html_file'):
        os.mkdir('ebay_laptop_html_file')

    page_queue = Queue(10)
    for i in range(1,11):
        page_queue.put(i)

    spider_list = ['spider1','spider2','spider3']
    thread_list = []

    for spider in spider_list:
        thread = page_download(spider,page_queue)
        thread.start()
        thread_list.append(thread)

    while not page_queue.empty():
        pass
    global Requests_Exit
    Requests_Exit = True

    for thread in thread_list:
        thread.join()

    total_time = time.time() - start_time
    print('Finish in ' + str(total_time) + '  seconds')



if __name__=='__main__':
    start_time = time.time()
    main()