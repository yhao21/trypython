import requests
from bs4 import BeautifulSoup
import glob
import os
import pandas as pd
if not os.path.exists("coinmk_data_file"):
    os.mkdir("coinmk_data_file")

df = pd.DataFrame()

for one_file in glob.glob("coin_market_html_file/*.html"):
    print("parsing:"+ one_file)
    scrapping_time = os.path.basename(one_file).replace("coinmarketcap","").replace("html","")

    f = open(one_file,"r",encoding="utf-8")
    soup = BeautifulSoup(f.read(),"html.parser")
    f.close()


    for items in soup.find_all("tr",class_="cmc-table-row"):
        try:
            link = items.find("td",class_="cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name").find("a").get('href')
            print(link)
            df = df.append({
                "link":link
            },ignore_index=True)
        except:
            pass
df.to_csv("links.csv")