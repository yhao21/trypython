import requests
from bs4 import BeautifulSoup


url = "https://www.thriftbooks.com/browse/?b.search=python#b.s=mostPopular-desc&b.p=1&b.pp=30&b.oos&b.tile"
kv = {"User-Agent" : "Mozilla/5.0"}

r = requests.get (url, headers = kv)
r.encoding = r.apparent_encoding



print (r.request.headers)