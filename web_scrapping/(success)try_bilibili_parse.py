import glob
import pandas as pd
from bs4 import BeautifulSoup

df = pd.DataFrame()

for one_file in glob.glob("bilibili_html_file/*.html"):
    f = open(one_file, "r", encoding="utf-8")
    soup = BeautifulSoup(f.read(),"html.parser")
    for items in soup.find_all("li",class_="video-item matrix"):
        link = items.a.attrs["href"]
        name = items.a.attrs["title"]
        view = items.find("div",class_="info").find("div",class_="tags").find("span",class_="so-icon watch-num").get_text().strip()
        release_time = items.find("div",class_="info").find("div",class_="tags").find("span",class_="so-icon time").get_text().strip()
        streamer = items.find("div",class_="info").find("div",class_="tags").find("a",class_="up-name").get_text().strip()
        df = df.append({
            "1.Video Name":name,
            "2.Streamer":streamer,
            "3.Release Time":release_time,
            "4.View Times":view,
            "5.Link":link
        },ignore_index = True)
print (df)
##为什么python可以识别文字内容，csv不能？？？
df.to_csv("bilibili_html_file/videos.csv", encoding="utf-8-sig")
