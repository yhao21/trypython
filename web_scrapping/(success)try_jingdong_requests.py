import os
import requests
import time


if not os.path.exists("jingdong_html_file"):
    os.mkdir("jingdong_html_file")
    if not os.path.exists("jingdong_html_file/pages"):
        os.mkdir("jingdong_html_file/pages")

# url = "https://search.jd.com/Search?keyword=%E6%98%BE%E5%8D%A1&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&page=1"
kv = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
# f = open("jingdong_html_file/pages/file.html","w",encoding="utf-8")
# r = requests.get(url, headers = kv)
# r.encoding = r.apparent_encoding
# html = r.text
# f.write(html)
# f.close()

for i in range(1,101):
    page = 2 * i - 1
    fullurl = "https://search.jd.com/Search?keyword=%E6%98%BE%E5%8D%A1&enc=utf-8&qrst=1&rt=1&stop=1&vt=2" + "&page=" + str(page)
    f = open ("jingdong_html_file/page number_" + str(i) +".html", "w", encoding="utf-8")
    r = requests.get(fullurl, headers = kv)
    r.encoding = r.apparent_encoding
    html = r.text
    f.write(html)
    f.close()
    print("Finish downloading page #" + str(i))
    time.sleep(1)


print("Finish!")

