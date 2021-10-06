import requests
import os
import datetime
import time

if not os.path.exists("coin_exchange_html_file"):
    os.mkdir("coin_exchange_html_file")



kv = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36"}
current_time = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d-%H-%M-%S")
for i in range(1,3):
    page_number = str(i)
    full_url = "https://coinmarketcap.com/rankings/exchanges/" + page_number + "/"
    f = open("coin_exchange_html_file/exchange_by_volume" + "page # " + page_number + " " +current_time + ".html","w",encoding="utf-8")
    r = requests.get(full_url,headers = kv)
    r.encoding = r.apparent_encoding
    f.write(r.text)
    f.close()
    print("finish downloading page #" + page_number)
