import glob
import pandas as pd
from bs4 import BeautifulSoup
import re

for one_file in glob.glob("re_steam_html_file/*.html"):
    f = open(one_file,"r",encoding="utf-8")






    # str = str(f.read())
    # result = re.compile(r"<br>(.*?)</div>").search(str)
    # print(result)
    # #     ###返回11.04变价后结果，