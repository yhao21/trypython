import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

df = pd.DataFrame()

url = "https://search.bilibili.com/all?keyword=%E5%8D%9A%E5%A3%AB&from_source=nav_search_new"
kv = {"User-Agent":"Mozilla/5.0"}
f = open("bilibili_html_file/text"+".html","w",encoding="utf-8")
r = requests.get(url,headers = kv)
r.encoding = r.apparent_encoding
html = r.text
####
soup = BeautifulSoup (html,"html.parser")
total_page = soup.find("div", class_="page-wrap").find("li", class_="page-item last").find("button",class_="pagination-btn").get_text().strip()
total_pages = int(total_page)
for page in range(1,total_pages + 1):
    fulurl = url + "&page=" + str(page)
    r = requests.get(fulurl, headers = kv)
    print ("downloading page #  " + str(page))
    r.encoding = r.apparent_encoding
    htmls = r.text
    soup = BeautifulSoup(htmls, "html.parser")
    for items in soup.find_all("li", class_="video-item matrix"):
        link = items.a.attrs["href"]
        name = items.a.attrs["title"]
        view = items.find("div", class_="info").find("div", class_="tags").find("span", class_="so-icon watch-num").get_text().strip()
        release_time = items.find("div", class_="info").find("div", class_="tags").find("span", class_="so-icon time").get_text().strip()
        streamer = items.find("div", class_="info").find("div", class_="tags").find("a", class_="up-name").get_text().strip()
        df = df.append({
            "1.Video Name": name,
            "2.Streamer": streamer,
            "3.Release Time": release_time,
            "4.View Times": view,
            "5.Link": link
        }, ignore_index=True)
    print("page #" + str(page) + "finished")
print(df)
##为什么python可以识别文字内容，csv不能？？？
df.to_csv("bilibili_html_file/videoss.csv")



