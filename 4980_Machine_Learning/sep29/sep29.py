import time, datetime
import urllib.request
import os, requests



if not os.path.exists('coin_file'):
    os.mkdir('coin_file')

for i in range(5):
    time_name = datetime.datetime.fromtimestamp(time.time()).\
            strftime('%Y-%m-%d-%H-%M-%S')


    f = open('coin_file/coin_mkt' + time_name + '.html', 'w')
    url = 'https://coinmarketcap.com/'
    r = requests.get(url)
    html = r.text
    f.write(html)
    f.close()


    print(time_name)
    time.sleep(1)
    
