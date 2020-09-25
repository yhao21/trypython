import os
import requests

if not os.path.exists("bwf_rank_html_file"):
    os.mkdir("bwf_rank_html_file")
kv = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
url = "https://bwfbadminton.com/rankings/"
f = open("bwf_rank_html_file/text" + ".html", "w", encoding="utf-8")
r = requests.get(url)
r.encoding = r.apparent_encoding
html = r.text
f.write(html)
f.close()
