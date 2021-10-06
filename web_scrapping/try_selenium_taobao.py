# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import os
#
# if not os.path.exists ("html_files"):
#     os.mkdir ("html_files")
#
# url = "https://s.taobao.com/search?q=1&type=p&tmhkh5=&spm=a21wu.241046-us.a2227oh.d100&from=sea_1_searchbutton&catId=100"
# f = open("html_files/taobao_1" + ".html", "w",encoding="utf-8")
# driver = webdriver.Chrome ()
# driver.get (url)
# html = driver.page_source
# f.write(html)
# f.close()

import glob
from bs4 import BeautifulSoup

for one_file_name in glob.glob("html_files/*.html"):
    f = open(one_file_name, "r", encoding="utf-8")
    soup = BeautifulSoup(f.read(), "html.parser")
    f.close()

    print (soup)


