import os
import requests
import datetime
import time


if not os.path.exists("univ_rank_html_file"):
    os.mkdir("univ_rank_html_file")

current_time_stamp = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d-%H-%M-%S")
f = open("univ_rank_html_file/text" + current_time_stamp + ".html","w",encoding="utf-8")
url = 'http://www.zuihaodaxue.com/Greater_China_Ranking2019_0.html'
r = requests.get(url)
r.encoding = r.apparent_encoding
html = r.text
f.write(html)
r.close()

