import glob
import pandas as pd
from bs4 import BeautifulSoup

df = pd.DataFrame()

for one_file in glob.glob("jingdong_html_file/*.html"):
    f = open(one_file, "r", encoding="utf-8")
    soup = BeautifulSoup(f.read(), "html.parser")
    for items in soup.find_all("li",class_="gl-item"):
        name = items.find("div",class_="gl-i-wrap").find("div",class_="p-name p-name-type-2").find("em").get_text().strip()
        price = items.find("div",class_="p-price").get_text().strip()
        seller = items.find("div",class_="p-shop").get_text().strip()
        ###京东评论标签下面明明有字符串，但是为什么不能显示
        comments = items.find("div",class_="p-commit").find("a").get_text()
        link = items.find("div",class_="gl-i-wrap").find("div",class_="p-name p-name-type-2").a.attrs["href"]
        df = df.append({
            "1.Product":name,
            "2.Price":price,
            "3.Seller":seller,
            "4.Comments":comments,
            "5.Links":link
        },ignore_index=True)
print(df)
df.to_csv("jingdong_html_file/data.csv",encoding="utf-8-sig")
####注意，使用utf-8-sig可以保证导出中文不乱码
