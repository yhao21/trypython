import requests
import os
import time
###注意：os查找路径是在python文件所在目录开始查起
if not os.path.exists("eastmoney_ppi_html_file"):
    os.mkdir("eastmoney_ppi_html_file")
    if not os.path.exists("eastmoney_ppi_html_file/pages"):
        os.mkdir("eastmoney_ppi_html_file/pages")



kv = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
for i in range (1,10):
    url = "http://data.eastmoney.com/cjsj/productpricesindex.aspx?p=" + str(i)
    f = open ("eastmoney_ppi_html_file/pages/page # " + str(i) + ".html", "w", encoding="utf-8")
    r = requests.get(url, headers = kv)
    r.encoding = r.apparent_encoding
    html = r.text
    f.write(html)
    f.close()
    print("Finish Downloading Page # " + str(i))
    time.sleep(1)

print ("Finish!")
