import os
import requests


if not os.path.exists ("coin_html_file"):
    os.mkdir("coin_html_file")

url = "https://coinmarketcap.com/"
f = open ("coin_html_file/text" + ".html", "w", encoding="utf-8")
r = requests.get (url)
r.encoding = r.apparent_encoding
html = r.text
f.write(html)
f.close()
