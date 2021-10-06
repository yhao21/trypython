import glob
import pandas as pd
from bs4 import BeautifulSoup

df = pd.DataFrame()

for one_file in glob.glob("bilibili_pubg_html_file/*.html"):
    f = open (one_file, "r", encoding = "utf-8")
    soup = BeautifulSoup(f.read(),"html.parser")
    items = soup.find_all("li",class_="video-item matrix")
    for item in items:
        video_name = item.a.attrs["title"]
        link = item.a.attrs["href"]
        watch_number = item.find("span",class_="so-icon watch-num").get_text().strip()
        review_number =item.find("span",class_="so-icon hide").get_text().strip()
        release_time = item.find("span",class_="so-icon time").get_text().strip()
        streamer = item.find("span",title = "up主").get_text().strip()
        df = df.append({
            "1.Video Name":video_name,
            "2.Streamer":streamer,
            "3.Release Time":release_time,
            "4.View Times":watch_number,
            "5.Review Number":review_number,
            "6.Link":link
        },ignore_index = True)
print (df)
df.to_csv("bilibili_pubg_html_file/videos.csv")