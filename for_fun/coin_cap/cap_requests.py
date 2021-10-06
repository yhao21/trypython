import requests


url = 'https://coinmarketcap.com/currencies/bitcoin/historical-data/?start=20130428&end=20200426'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36'}

r = requests.get(url, headers = headers)
html = r.text


with open('cap.html','w', encoding = 'utf-8') as f:
    f.write(html)
    f.close()
