import pandas as pd
from bs4 import BeautifulSoup
import glob, os



one_file = os.path.join(os.getcwd(), 'html_file', 'Page0.html')
print(one_file)

with open(one_file, 'r') as f:
    html = f.read()

res = []
df = pd.DataFrame()
soup = BeautifulSoup(html, 'html.parser')
rows = soup.find('tbody').find_all('tr', \
        {'class':'rc-table-row rc-table-row-level-0 cmc-table-row'})
for row in rows:
    tds = row.find_all('td')
    name = tds[2].find('div').find('p').string
    price = tds[3].find('a').string.replace('$','')
    sub_link = tds[2].find('a')['href']
    link = 'https://coinmarketcap.com' + sub_link

    df = df.append({
        'name':name,
        'price':price,
        'link':link
        },ignore_index = True)


print(df)

order = ['name','price','link']
df = df[order]
print(df)
