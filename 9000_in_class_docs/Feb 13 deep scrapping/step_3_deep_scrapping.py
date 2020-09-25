import time
import requests
import re
import os
import pandas as pd

if not os.path.exists("deep_scrapping_html"):
    os.mkdir("deep_scrapping_html")
df = pd.read_csv("links.csv")
##检查是否成功导入
# print(df)
# ##只打印link列
# print(df['link'])

for link in df['link']:
    # print(link)
    kv = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
    url = 'https://coinmarketcap.com' + link
    # print(url)
    ###tom 的方法
    ###file_name = link.replace('/',"").replace('currencies',"")
    file_name = re.compile(r'/currencies/(.*)\/').findall(url)
    print(file_name)
    if not os.path.exists("deep_scrapping_html/" + str(file_name) + ".html"):
        f = open("deep_scrapping_html/" + str(file_name) + '.html.temp',"w",encoding="utf-8")
        r = requests.get(url,headers = kv)
        r.encoding = r.apparent_encoding
        html = r.text
        f.write(html)
        f.close()
        print("finish downloading : " + str(file_name))
        os.rename("deep_scrapping_html/" + str(file_name) + '.html.temp',"deep_scrapping_html/" + str(file_name) + '.html')
        time.sleep(20)
    else:
        print('file exist')
"""
如何断点续传：
在requests之前查看是否已经存在该文件

但如果文件建立但是在requests过程程序中断，如何解决：
创建html.temp file
完全下载后重新命名文件为file_name

此方法亦可作为检查页面是否下载完整的方法

"""


