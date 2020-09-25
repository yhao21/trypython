import glob
import pandas as pd
from lxml import etree

df = pd.DataFrame()

for one_file in glob.glob("univ_rank_html_file/text2020-02-07-15-36-59.html"):
    f = open(one_file, "r", encoding="utf-8")
    content = f.read()
    tree = etree.HTML(content)
    ranks = tree.xpath('//tbody/tr/td[1]/text()')
    univs = tree.xpath('//td[@class="align-left"]/a/div/text()')
    regions = tree.xpath('//tbody/tr/td[3]/text()')
    total_scores = tree.xpath('//tbody/tr/td[4]/text()')
    for i in range(len(ranks)):
        rank = ranks[i]
        univ = univs[i]
        region = regions[i]
        total_score = total_scores[i]
        df = df.append({
            "1.Rank":rank,
            "2.University":univ,
            "3.Region":region,
            "4.Total Score":total_score
        },ignore_index=True)


print(df)