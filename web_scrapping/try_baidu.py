import requests
from bs4 import BeautifulSoup


url = "http://www.baidu.com/"
r = requests.get(url)
r.encoding = r.apparent_encoding
html = r.text

soup = BeautifulSoup (html, "html.parser")
# for title in soup.find_all ("a"):
#     print (title)
# print (soup.prettify())
###???为什么找不到“时事热点”的标签，直接搜索某一条时事热点题目所在的a标签也搜索不到

div = soup.find_all ("div")
print (div)


