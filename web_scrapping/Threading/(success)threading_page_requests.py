import threading
import requests
import os
from queue import Queue
import time


Requests_Exit = False

if not os.path.exists("coinmarketcap_html_file"):
    os.mkdir("coinmarketcap_html_file")

class ThreadSpider(threading.Thread):
    def __init__(self, spider, page_queue):
        super().__init__()
        self.spider = spider
        self.page_queue = page_queue
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    def run(self):
        while not Requests_Exit:
            try:
                page_number = self.page_queue.get(False)
                f = open("coinmarketcap_html_file/page # " + str(page_number) + ".html","w",encoding = "utf-8")
                url = "https://coinmarketcap.com/" + str(page_number) +"/"
                r = requests.get(url,headers = self.headers)
                r.encoding = r.apparent_encoding
                f.write(r.text)
                f.close()
                print("finish downloading page #" + str(page_number))
            except:
                pass

def main():
    page_queue = Queue(10)
    for i in range(1,11):
        page_queue.put(i)

    spiderlist = ["spider1","spider2","spider3","spider4","spider5"]
    threadspider = []
    for spider in spiderlist:
        thread = ThreadSpider(spider,page_queue)
        thread.start()
        threadspider.append(thread)

    while not page_queue.empty():
         pass
    global Requests_Exit
    Requests_Exit = True

    for thread in threadspider:
        thread.join()
    total_time = time.time() - start_time
    print("total time: ",total_time)


if __name__=="__main__":
    start_time = time.time()
    main()