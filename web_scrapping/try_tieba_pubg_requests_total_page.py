import os
import glob
import requests
from bs4 import BeautifulSoup
import re
import numpy as np
import pandas as pd


if not os.path.exists("tieba_pubg_html_file"):
    os.mkdir("tieba_pubg_html_file")
if not os.path.exists("tieba_pubg_html_file/pages"):
        os.mkdir("tieba_pubg_html_file/pages")
#


url = "https://tieba.baidu.com/f?kw=pubg&ie=utf-8&pn=0"
kv = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
f = open("tieba_pubg_html_file/page"+'.html',"w",encoding="utf-8")
r = requests.get(url, headers = kv)
# content=r.headers["content-type"]

"""返回：text/html; charset=UTF-8
若本身网页就是utf-8，无需下面的转码，直接保存就可以，以避免乱码
"""
# r.encoding = r.apparent_encoding
html = r.text

f.write(html)
f.close()


