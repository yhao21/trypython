import urllib.request
import os
import time
import datetime

"""
put a time stamp
os包允许在python中使用dos命令
"""
if not os.path.exists ("coin_market_html_file"):
    os.mkdir("coin_market_html_file")

for i in range(11):
    ##capital sensitive,,,little m and d,,,strftime用来设置格式
    current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y%m%d%H%M%S")

    f = open("coin_market_html_file/coinmarketcap" + current_time_stamp + ".html","wb")

    url = "https://coinmarketcap.com/"
    response = urllib.request.urlopen(url)
    print (response)
    """
    返回：<http.client.HTTPResponse object at 0x000001E56DE17DC0>
    """
    html = response.read()
    print(html)
    f.write(html)
    f.close()
    # time.sleep(5 + i + 10)
    """
    躲避反爬虫：
    1. 间隔时间尽量不要相等，可以在后面加一些，比如加上i+20
    2. 可以让程序在下载玩一次url后，进入该网页其他的连接，然后再回到这个url
    """

#每间隔5秒，下载一次页面





