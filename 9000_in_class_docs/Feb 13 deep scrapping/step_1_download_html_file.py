import time
"""
ctr +shift + p在sublime 中，打开搜索栏，可以安装各种package
"""
import urllib.request
import os
import time
import datetime


if not os.path.exists ("coin_market_html_file"):
    os.mkdir("coin_market_html_file")

for i in range(5):
    current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")
    f = open("coin_market_html_file/coinmarketcap" + current_time_stamp + ".html","wb")
    url = "https://coinmarketcap.com/"
    response = urllib.request.urlopen(url)
    print (response)
    html = response.read()
    print(html)
    f.write(html)
    f.close()
"""
不仅下载text，also href。link
"""






