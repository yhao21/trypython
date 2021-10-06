import os
import requests



if not os.path.exists ("html_files_taobao"):
    os.mkdir ("html_files_taobao")

url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313.TR12.TRC2.A0.H0.Xvideo+card.TRS0&_nkw=video+card&_sacat=0"
f = open("html_files_taobao/1" + ".html", "w", encoding="utf-8")
r = requests.get(url)
r.encoding = r.apparent_encoding
f.write(r.text)
f.close()



