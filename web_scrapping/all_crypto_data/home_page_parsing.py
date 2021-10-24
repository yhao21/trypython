from bs4 import BeautifulSoup
import pandas as pd
import os, glob, re




df = pd.DataFrame()
file_folder = 'html_dir'

i = 1
for one_file in glob.glob(os.path.join(file_folder, '*.html')):
    workload = len(glob.glob(os.path.join(file_folder, '*.html')))
    print(f'[{i}/{workload}]')

    with open(one_file, 'r') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    rows = soup.find('tbody').find_all('tr')
    for row in rows:
        tds = row.find_all('td')
        href = 'https://www.coingecko.com' + tds[2].a.attrs['href']
        name = re.compile(r'coins/(.*)').findall(href)[0].replace('/','')
        price = tds[3].find('span').get_text().replace('$','')
        mktcap = tds[8].get_text().replace('\n','').replace('$','')

        if '?' not in mktcap:
            df = df.append({
                'name':name,
                'price':price,
                'mktcap':mktcap,
                'href':href
                },ignore_index = True)
        else:
            print(f'{name}: No mktcap info.')

    i += 1

df = df[['name','price','mktcap','href']]
print(df)
df.to_csv('csv_folder/homepage_crypto_href.csv', index = False)
