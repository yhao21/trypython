import os
import requests

if not os.path.exists("coin_trend_html_file"):
    os.mkdir("coin_trend_html_file")

url = "https://coinmarketcap.com/currencies/bitcoin/"
kv = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
f = open("coin_trend_html_file/text" + ".html", "w", encoding="utf-8")
r = requests.get(url, headers = kv)
r.encoding = r.apparent_encoding
html = r.text
f.write(html)
f.close()