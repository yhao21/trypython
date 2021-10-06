import glob
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame()

for one_file in glob.glob("bwf_rank_html_file/*.html"):
    f = open (one_file, "r", encoding = "utf-8")
    soup = BeautifulSoup (f.read(), "html.parser")
    for items in soup.find("tbody").find_all("tr"):
        try:
            rank = items.find("td",align = "center").string
            ##不想通过去除字符串空格来获取精确文本，发现下一级img标签的title内容与我想获得的内容相符，故，取title内容
            countries = items.find("div",class_="country").img.attrs["title"]
            players = items.find("div",class_="player").a.attrs["title"]
            ##.trip()可以去除字符串左右的空格
            win_loss = items.find("td",align = "center",class_="mobile").find_next_sibling().get_text().strip()
            ##因标签无特殊区别，只能通过平行标签查找，，，脑壳疼
            prize_money = items.find ("td",align="center", class_="mobile").find_next_sibling().find_next_sibling().get_text()
            points_tournaments = items.find("td",align="center",class_="point").find("strong").get_text()
            # print(win_loss)
            df = df.append({
                "1.Rank":rank,
                "2.Country/Territory":countries,
                "3.Players":players,
                "4.Win/Loss":win_loss,
                "5.Prize Money":prize_money,
                "6.Points/Tournaments":points_tournaments
            },ignore_index=True)
        except:
            pass

print (df)
df.to_csv("bwf_rank_html_file/rank_data.csv")