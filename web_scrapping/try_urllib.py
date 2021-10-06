import urllib.request
import os
import time
import datetime

url ="https://s.taobao.com/search?q=1&type=p&tmhkh5=&spm=a21wu.241046-us.a2227oh.d100&from=sea_1_searchbutton&catId=100"
##判断是否存在名为html_files的文件夹，若没有，则创建一个
if not os.path.exists("html_files"):
    os.mkdir ("html_files")
##在html_files文件夹下创建taobao_1.html文件，设置为可读写模式（若该文件中已存在内容，则先清空再写入）
f = open ("html_files/taobao_1" + ".html", "wb")
r = urllib.request.urlopen (url)
html = r.read()
f.write(html)
f.close()


import glob
from bs4 import BeautifulSoup

for one_file_name in glob.glob ("html_files/*.html"):
    f = open (one_file_name, "r")
    soup = BeautifulSoup (f.read(), "html.parser")
    # print (soup)

div_tage = soup.find_all ("div", class_="item J_MouserOnverReq ")
print (div_tage)