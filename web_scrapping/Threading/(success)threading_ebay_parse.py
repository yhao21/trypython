import re
import os
import glob
from queue import Queue
import threading
import pandas as pd

"""
ebay标签结构有些混乱，故使用re直接查找
"""

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
                file_root = self.file_queue.get(False)
                file_name = re.compile(r'.*?\\(.*?)\.html').findall(file_root)

                if not os.path.exists('ebay_laptop_html_file/' + str(file_name) + '.csv'):
                    f = open(file_root,'r',encoding = 'utf-8')
                    html = f.read()
                    f.close()
                    names = re.compile(r'<a href="https://www.ebay.com/itm/(.*?)/\d*').findall(html)
                    prices = re.compile(r's-item__price">(.*?)<').findall(html)
                    ##freeship和收运费的商品在其运费信息所在标签不同，所以，要先获得整个运费标签，然后对那些freeshipping的商品，去掉<span class="BOLD">
                    shipcost = re.compile(r's-item__shipping s-item__logisticsCost">(.*?)</span').findall(html)
                    ship_costs = []
                    for item in shipcost:
                        freeshipping = item.replace('<span class="BOLD">','')
                        ship_costs.append(freeshipping)

                    for i in range(len(names)):
                        name = names[i]
                        price = prices[i]
                        ship_cost = ship_costs[i]

                        df = df.append({
                            "name":name,
                            "price":price,
                            "ship cost":ship_cost
                        },ignore_index = True)

                    print(df)
                    df.to_csv('ebay_laptop_html_file/' + str(file_name) + '.csv')

                else:
                    print('Data file ' + str(file_name) + '.csv' + ' is existed')

            except:
                pass

def main():
    files = glob.glob('ebay_laptop_html_file/*.html')
    file_queue = Queue()
    for file in files:
        file_queue.put(file)

    parser_list = ['parser1','parser2','parser3']
    thread_list = []
    for parser in parser_list:
        thread = page_parsing(parser,file_queue)
        thread.start()
        thread_list.append(thread)

    while not file_queue.empty():
        pass

    global Parse_Exit
    Parse_Exit = True

    for thread in thread_list:
        thread.join()


if __name__=="__main__":
    main()