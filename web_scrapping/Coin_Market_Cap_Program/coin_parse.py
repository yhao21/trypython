from bs4 import BeautifulSoup
import glob
import pandas as pd

df = pd.DataFrame()

for one_file in glob.glob("coin_exchange_html_file/*.html"):
    f = open(one_file,"r",encoding="utf-8")
    soup = BeautifulSoup(f.read(),"html.parser")
    rows = soup.find("tbody").find_all("tr")
    for items in rows:
        tds = items.find_all("td")
        coin_rank = tds[0].string
        coin_name = tds[1].find('a').string
        adj_vol_24 = tds[2].find('a').string
        vol_24 = tds[3].find('a').string
        vol_7days = tds[4].find('a').string
        vol_30days = tds[5].find('a').string
        df = df.append({
            "1.Coin Rank":coin_rank,
            "2.Coin Name":coin_name,
            "3.Adj. Vol 24hr":adj_vol_24,
            "4.Vol_24hr":vol_24,
            "5.Vol_7days":vol_7days,
            "6.Vol_30days":vol_30days
        },ignore_index=True)

print(df)
df.to_csv("coin_vol_data.csv",encoding="utf-8")