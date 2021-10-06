from bs4 import BeautifulSoup
import glob
import pandas as pd

df = pd.DataFrame()


for one_file in glob.glob("tieba_pubg_html_file/pages/*.html"):
    f = open(one_file, "r", encoding="utf-8")
    soup = BeautifulSoup(f.read(),"html.parser")
    rows = soup.find('div',id="pagelet_frs-list/pagelet/thread_list").find('ul',id="thread_list").find_all('li')
    for items in rows:
        try:
            name = items.find('div',class_="t_con cleafix").find('a',class_="j_th_tit").get_text()
            author = items.find('span',class_="frs-author-name-wrap").get_text()
            df = df.append({
                "1.Name":name,
                "2.Author":author,
            },ignore_index=True)
        except:
            pass
print(df)
df.to_csv("tieba_pubg_html_file/content.csv",encoding="utf-8-sig")