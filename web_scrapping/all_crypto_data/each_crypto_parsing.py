from bs4 import BeautifulSoup
import pandas as pd
import os, re, glob



def converter(input_str):
    if '?' in input_str:
        input_str = 'NIF'
    elif '∞' in input_str:
        input_str = 'infinite'
    else:
        input_str = float(input_str)
    return input_str



file_folder = 'each_crypto'
df = pd.DataFrame()


i = 1
workload = len(glob.glob(os.path.join(file_folder, '*.html')))
for one_file in glob.glob(os.path.join(file_folder, '*.html')):

    name = re.compile(r'each_crypto/(.*).html').findall(one_file)[0]
    print(f'[{i}/{workload}] {name}')

    with open(one_file, 'r') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')
    try:
        supply_text = soup.find('div',{"class":"tw-col-span-2 lg:tw-col-span-2"})\
                .find('div',{'class':'tw-flex flex-wrap lg:tw-pl-4'}).find_all('div')[2]\
                .get_text().replace('\n','')
        max_supply = re.compile(r'Supply(.*)').findall(supply_text)[0].replace(',','')
        max_supply = converter(max_supply)
    except:
        max_supply = 'NIF'

    try:

        sub_href = soup.find('div',{'class':'coin-card'}).find('ul',{'class':'nav primary-tabs tw-border-solid tw-border-b tw-border-t-0 tw-border-l-0 tw-border-r-0 tw-border-gray-200 dark:tw-border-opacity-10 pb-0'}).find_all('li')[3].a.attrs['href']\
                .replace('#panel','?start_date=2012-01-01&end_date=2021-10-05#panel')
        href = 'https://www.coingecko.com' + sub_href
        df = df.append({
            'name':name,
            'max_supply':max_supply,
            'href':href
            },ignore_index = True)
    except:
        print('No historical data')

    i += 1

df = df[['name','max_supply','href']]
print(df)
df.to_csv('csv_folder/each_crypto.csv', index = False)



