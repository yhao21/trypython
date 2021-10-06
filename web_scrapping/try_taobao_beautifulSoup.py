import requests
from bs4 import BeautifulSoup

url = "https://s.taobao.com/search?q=%E5%B8%86%E5%B8%83%E9%9E%8B&type=p&tmhkh5=&spm=a21wu.241046-us.a2227oh.d100&from=sea_1_searchbutton&catId=100"

r = requests.get(url)
r.encoding = r.apparent_encoding
html = r.text
soup = BeautifulSoup (html, "html.parser")
# for a in soup.find_all("a", class_="J_ClickStat"):
# #     print (a)
# # ###这个a标签在后台代码中指代商品名称
# # ###???为什么找不到

##打印所有tag下的字符串（包含所有子节点的字符串）
# for string in soup.strings:
#     print (repr(string))

print (soup.find("body",class_="response-narrow"))