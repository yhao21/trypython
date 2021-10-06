import glob
import pandas as pd
from bs4 import BeautifulSoup

df = pd.DataFrame ()

for one_file in glob.glob("coin_trend_html_file/*.html"):
    f = open(one_file,"r",encoding="utf-8")
    soup = BeautifulSoup(f.read(),"html.parser")
    price = soup.find("g")
    print(price)