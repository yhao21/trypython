import requests
from bs4 import BeautifulSoup

url = "https://baidu.com"

kv = {"user-agent":"Mozilla/5.0"}
r = requests.get(url, headers = kv)
r.encoding = r.apparent_encoding
print(r.status_code)
####cueb 网站访问报错

