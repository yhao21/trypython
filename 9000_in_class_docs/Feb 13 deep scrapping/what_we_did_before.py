from bs4 import BeautifulSoup
import glob
import pandas as pd
import os

if not os.path.exists("coinmk_data_file"):
    os.mkdir("coinmk_data_file")

df = pd.DataFrame()

for one_file in glob.glob("coin_market_html_file/*.html"):
    print("parsing:"+ one_file)
    ##去掉名字中非时间部分
    scrapping_time = os.path.basename(one_file).replace("coinmarketcap","").replace("html","")

    f = open(one_file,"r",encoding="utf-8")
    soup = BeautifulSoup(f.read(),"html.parser")
    ##读完文档注意关闭，，，不需要每次都read，，占资源，速度慢
    f.close()


    for items in soup.find_all("tr",class_="cmc-table-row"):
        try:
            name = items.find("td",class_="cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name").find("a").get_text().strip()
            mkt_cap = items.find("td",class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap").find("div").get_text().strip()
            price = items.find("td",class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price").find("a").get_text().strip().replace(",","").replace("$","")
            Volume_24hr = items.find("td",class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__volume-24-h").find("a").get_text().strip()
            ##通过replace函数替换不需要的内容
            circulating_supply = items.find("td",class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply").find("div").get_text().strip().replace(" *","")
            change = items.find("td",class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-24-h").find("div").get_text().strip()
            link = items.find("td",class_="cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name").find("a").get('href')
            print(link)
            df = df.append({
                "Time":scrapping_time,
                "name":name,
                "mkt_cap":mkt_cap,
                "price":price,
                "Volume_24hr":Volume_24hr,
                "Circulating_supply":circulating_supply,
                "change":change,
                "Currency_Link":link
            },ignore_index=True)
        except:
            pass
#     print(df)
# df.to_csv("coinmk_data_file/coinmktcap_data.csv",encoding="utf-8-sig")