import requests
from bs4 import BeautifulSoup

url = "https://s.taobao.com/search?q=1&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20200123&ie=utf8"

r = requests.get(url)
r.encoding = r.apparent_encoding
web_text = r.text

soup = BeautifulSoup(web_text, "html.parser")
links = soup.find_all ("a", class_="J_ClickStat")

print (links)

