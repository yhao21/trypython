from bs4 import BeautifulSoup
import glob
import pandas as pd


df = pd.DataFrame ()

for one_file in glob.glob("coin_html_file/*.html"):
    f = open (one_file, "r", encoding="utf-8")
    soup = BeautifulSoup (f.read(), "html.parser")
    for coins in soup.find_all ("tr", class_="cmc-table-row"):
        ##注意，一定要逐层提取，否则会与其他有相似标签名的标签冲突##
        items_name = coins.find("td", class_="cmc-table__cell cmc-table__cell--sticky cmc-table__cell--sortable cmc-table__cell--left cmc-table__cell--sort-by__name").find("div",class_="cmc-table__column-name sc-1kxikfi-0 eTVhdN").find("a").text
        items_mktcap = coins.find("td",class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__market-cap").find("div").text
        items_price = coins.find("td",class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__price").find("a").text
        items_volume = coins.find("td",class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__volume-24-h").find("a").text
        ##为什么输出的cirsupply后面有*，代码中是没有的##
        items_cirsupply = coins.find("td",class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__circulating-supply").find("div").text
        items_change = coins.find("td",class_="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-24-h").find("div").text

        df = df.append({
            "name":items_name,
            "market cap":items_mktcap,
            "price":items_price,

        }, ignore_index=True)

print (df)
# df.to_csv("coin_html_file/coinmarket_data.csv")
