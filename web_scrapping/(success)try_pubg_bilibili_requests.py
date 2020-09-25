import os
import requests
from bs4 import BeautifulSoup

if not os.path.exists("bilibili_pubg_html_file"):
    os.mkdir("bilibili_pubg_html_file")

url = "https://search.bilibili.com/all?keyword=pubg&from_source=nav_search_new"
kv = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
r = requests.get(url, headers = kv)
r.encoding = r.apparent_encoding
html = r.text
soup = BeautifulSoup (html,"html.parser")
total_page_number = int(soup.find("li",class_="page-item last").find("button",class_="pagination-btn").get_text().strip())
for page in range (1,total_page_number + 1):
    page_url = url + "&page=" + str(page)
    f = open("bilibili_pubg_html_file/%s"%str(page) + ".html","w",encoding="utf-8")
    r = requests.get(page_url,headers = kv)
    r.encoding = r.apparent_encoding
    html = r.text
    f.write(html)
    f.close()
    print("Finish downloading page #  "+str(page))





