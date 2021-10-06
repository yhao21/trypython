import os
import requests
import time

if not os.path.exists("thriftbooks"):
    os.mkdir("thriftbooks")

url = "https://search.jd.com/Search?keyword=%E6%89%8B%E8%A1%A8&enc=utf-8&wq=&pvid=17241a987def4720ac96f48c082c1909"
kv = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"
    }
f = open ("thriftbooks/text" + ".html", "w", encoding="utf-8")
r = requests.get(url,headers = kv)
r.encoding = r.apparent_encoding
html = r.text
# time.sleep(10)
# ##并非因为等待加载时间不足###
f.write(html)
f.close()

###被检查到使用爬虫，，如何绕过或通过检测？？##