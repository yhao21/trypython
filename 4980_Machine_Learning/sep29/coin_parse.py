import pandas as pd
from bs4 import BeautifulSoup
import os, glob



if not os.path.exists("parsed_file"):
    os.mkdir('parsed_file')

df = pd.DataFrame()

for one_file in glob.glob("coin_file/*.html"):
    name = os.path.basename(one_file).replace('coin_mkt','').replace(".html",\
            '')
    f = open(one_file, 'r')
    soup = BeautifulSoup(f.read(), 'html.parser')
    f.close()
    
    #rows = soup.find('tbody').find_all('tr')
    c_table = soup.find('tbody')
    rows = c_table.find_all('tr')
    print(len(rows))
    for r in rows:
        tds = r.find_all('td')
        #print(len(tds))
        ## some row does not have td, we need to debug and skip them.
        if len(tds) > 10:
            price = tds[3].find('a',{'class':'cmc-link'}).string.replace('$','').replace(',','')
            name = tds[2].find('p').string
            symbol = tds[2].find('p', {'class':'Text-sc-1eb5slv-0 eweNDy coin-item-symbol'}).string
            volume = tds[6].find('p',{'class':'Text-sc-1eb5slv-0 hVAibX'}).string.replace('$','').replace(',','')
            link_a = tds[2].find('a')['href']
            link = 'https://coinmarketcap.com' + link_a
    
            df = df.append({
                'name':name,
                'price':price,
                'symbol':symbol,
                'volume':volume,
                'link':link
                },ignore_index = True)

    print(df)

df.to_csv('coin_csv.csv')
    



