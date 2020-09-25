import os
import requests

if not os.path.exists("coin_mkt_cap_html_file"):
    os.mkdir("coin_mkt_cap_html_file")
f = open("coin_mkt_cap_html_file/#1.html","w",encoding="utf-8")
url = "https://coinmarketcap.com/rankings/exchanges/"
r = requests.get(url)
r.encoding = r.apparent_encoding
html = r.text
f.write(html)
f.close()
