import requests
from bs4 import BeautifulSoup
#
# url = "https://flights.ctrip.com/?&AllianceID=564348&sid=1477056"
#
# kv = {"user-agent":"Mozilla/5.0"}
# r = requests.get(url, headers = kv)
# r.encoding = r.apparent_encoding
#
# soup = BeautifulSoup (r.text, "html.parser")
# wrapped_dta = soup.find_all("div", class_="airline_item")
# for item in wrapped_dta:
#     airline_company = item.a.string
#     print (item.a)
###以上测试成功读取航空公司名称



url = "https://flights.ctrip.com/itinerary/oneway/sha-bjs?date=2020-01-27&sortByPrice=true#ctm_ref=fld_hp_rec_fav_t_1"

r = requests.get(url)
r.encoding = r.apparent_encoding

soup = BeautifulSoup (r.text, "html.parser")

print (soup.find_all("div", class_="cabinV2"))