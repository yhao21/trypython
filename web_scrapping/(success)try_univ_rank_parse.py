import glob
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame()

for one_file in glob.glob("univ_rank_file/*.html"):
    f = open (one_file, "r", encoding="utf-8")
    soup = BeautifulSoup (f.read(), "html.parser")
    for items in soup.find("tbody").find_all("tr"):
        ##只有名字所在标签信息和别标签不同
        univ_name = items.find("a").get_text()
        ##无法通过标签属性信息定位排名、地区、总分等，，只能通过在列表中的排位顺序了，，待寻找更优解。。。
        tds = items.find_all("td")
        univ_rank = tds[0].string
        univ_region = tds[2].string
        total_score = tds[3].string
        df = df.append({
            "1.University Rank":univ_rank,
            "2.University Name":univ_name,
            "3.University Region":univ_region,
            "4.Total Score": total_score
        },ignore_index=True)

print(df)
##须学习如何输出时就将每列的先后顺序排列好。pandas默认是字母和数字排序。。头疼
df.to_excel("univ_rank_file/rank.xls")

