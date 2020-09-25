import glob
from bs4 import BeautifulSoup
import pandas as pd


df = pd.DataFrame()

for one_file in glob.glob("stats_gov_html_file/text.html"):
    f = open(one_file,"r",encoding="utf-8")
    soup = BeautifulSoup(f.read(),"html.parser")
    print(soup.find('tbody'))