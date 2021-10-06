import os
import requests
import time

if not os.path.exists("eastmoney_cpi_html_file"):
    os.mkdir("eastmoney_cpi_html_file")
    if not os.path.exists("eastmoney_cpi_html_file/pages"):
        os.mkdir("eastmoney_cpi_html_file/pages")

# url = "http://data.eastmoney.com/cjsj/cpi.html"
kv = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}

for i in range(1,9):
    fullurl = "http://data.eastmoney.com/cjsj/consumerpriceindex.aspx?p=" + str(i)
    f = open("eastmoney_cpi_html_file/pages/page # " + str(i) + ".html", "w", encoding="utf-8")
    r = requests.get(fullurl, headers = kv)
    r.encoding = r.apparent_encoding
    html = r.text
    f.write(html)
    f.close()
    print("Finish downloading page #" + str(i))
    time.sleep(1)
print("Finish!")

