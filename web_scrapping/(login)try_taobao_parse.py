import glob
from bs4 import BeautifulSoup
import pandas as pd

# df = pd.DataFrame()

for file_taobao in glob.glob ("html_files_req_taobao/*.html"):
    f = open (file_taobao, "r", encoding="utf-8")
    soup = BeautifulSoup (f.read(), "html.parser")
    f.close()
    items_row = soup.find_all ("a", class_="J_ClickStat")
    print (items_row)
