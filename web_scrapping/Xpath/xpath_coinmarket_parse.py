from lxml import etree
import glob
import pandas as pd

df = pd.DataFrame()

for one_file in glob.glob("coin_mkt_cap_html_file/#1.html"):
    f = open(one_file, "r", encoding="utf-8")
    content = f.read()
    """
    注意：把读取的html文档通过etree解析后付给一个变量，然后所有的xpath都要在这个tree变量后进行
    """
    tree = etree.HTML(content)
    coin_name = tree.xpath('//div[@class="sc-1jx94bq-0 dWwPjl"]/a/text()')
    adj_vol_24hrs = tree.xpath('//td[@class="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__volume-24-h-adjusted"]/div/a/text()')
    vol_24hrs = tree.xpath('//td[@class="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__volume-24-h"]/div/a/text()')
    vol_7days = tree.xpath('//td[@class="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__volume-7-d"]/div/a/text()')
    vol_30days = tree.xpath('//td[@class="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__volume-30-d"]/div/a/text()')
    num_mkts = tree.xpath('//td[@class="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__num-market-pairs"]/div/a/text()')
    changes = tree.xpath('//td[@class="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__percent-change-volume-24-h"]/div/text()')
    launcheds = tree.xpath('//td[@class="cmc-table__cell cmc-table__cell--sortable cmc-table__cell--right cmc-table__cell--sort-by__date-launched"]/div/text()')
    for i in range(len(changes)):
        name = coin_name[i]
        adj_vol_24hr = adj_vol_24hrs[i]
        vol_24hr = vol_24hrs[i]
        vol_7day = vol_7days[i]
        vol_30day = vol_30days[i]
        num_mkt = num_mkts[i]
        change = changes[i]
        launched = launcheds[i]
        df = df.append({
            "1.Name":name,
            "2.Adj_Vol_24hrs":adj_vol_24hr,
            "3.Vol_24hrs":vol_24hr,
            "4.Vol_7days":vol_7day,
            "5.Vol_30days":vol_30day,
            "6.Num_MKTs":num_mkt,
            "7.Changes":change,
            "8.Launched":launched
        },ignore_index=True)
print(df)


