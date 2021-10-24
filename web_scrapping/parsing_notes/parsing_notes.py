

'''
1. replace blank space from the return value of get_text()

?


?

mktcap = tds[8].get_text().replace('\n','')
'''


import pandas as pd
from bs4 import BeautifulSoup
import re





file_path = 'html_folder/page_1.html'

with open(file_path, 'r') as f:
    html = f.read()
soup = BeautifulSoup(html, 'html.parser')
table = soup.find('tbody')


# extract ALL data in one line... NB!
data = [[td.text.strip() for td in tr.findChildren('td')] for tr in table.findChildren('tr')]

df = pd.DataFrame(data, columns = ['blank','rank','name', 'price','1h', '24hr','7d','24h_vol','mktcap','graph'])
df.drop(['blank','rank','graph'], axis = 1, inplace = True)


print(df)

price = df['price'].values
price = [float(i.replace('$','').replace(',','')) for i in price]
df['price'] = price

name = df['name'].values
name = [re.compile(r'(.*)\n').findall(i)[0].replace(' ','') for i in name]
df['name'] = name

## You can also write these three line in one line
df['1h'] = [float(i.replace('%','')) for i in df['1h'].values]
df['24hr'] = [float(i.replace('%','')) for i in df['24hr'].values]
df['7d'] = [float(i.replace('%','')) for i in df['7d'].values]
df['24h_vol'] = [float(i.replace('$','').replace(',','')) for i in df['24h_vol'].values]
df['mktcap'] = [float(i.replace('$','').replace(',','')) for i in df['mktcap'].values]
print(df)

'''
After

                   name         price   1h  24hr    7d       24h_vol        mktcap
0               Bitcoin  54346.000000  0.7   0.3  12.8  3.414968e+10  1.023375e+12
1              Ethereum   3580.300000  0.5  -0.7   8.3  1.828569e+10  4.213423e+11
2               Cardano      2.250000  0.8  -1.7   0.1  1.545273e+09  7.196197e+10
3                Tether      1.000000  0.2  -0.0   0.0  7.466760e+10  6.943362e+10
4           BinanceCoin    422.040000  0.8  -4.3   0.1  2.706805e+09  6.515963e+10
..                  ...           ...  ...   ...   ...           ...           ...
95          BitcoinGold     66.210000  0.4  -3.9  16.3  1.849141e+07  1.163312e+09
96        CurveDAOToken      2.930000  0.5   4.8  15.7  1.924000e+08  1.153828e+09
97   MagicInternetMoney      1.010000  0.2  -0.4   0.5  4.675276e+07  1.147280e+09
98            Ravencoin      0.112977  0.3  -0.4   6.5  5.120012e+07  1.109215e+09
99  DecentralizedSocial    105.290000 -1.3  -6.7 -33.3  2.751780e+05  1.108886e+09

[100 rows x 7 columns]


Before:
                                      name      price     1h   24hr      7d          24h_vol              mktcap
0                  Bitcoin\n \nBTC\n \nBTC    $54,346   0.7%   0.3%   12.8%  $34,149,680,566  $1,023,375,336,607
1                 Ethereum\n \nETH\n \nETH  $3,580.30   0.5%  -0.7%    8.3%  $18,285,690,341    $421,342,269,350
2                  Cardano\n \nADA\n \nADA      $2.25   0.8%  -1.7%    0.1%   $1,545,272,758     $71,961,969,410
3                 Tether\n \nUSDT\n \nUSDT      $1.00   0.2%  -0.0%    0.0%  $74,667,596,938     $69,433,624,297
4             Binance Coin\n \nBNB\n \nBNB    $422.04   0.8%  -4.3%    0.1%   $2,706,804,587     $65,159,629,040
..                                     ...        ...    ...    ...     ...              ...                 ...
95            Bitcoin Gold\n \nBTG\n \nBTG     $66.21   0.4%  -3.9%   16.3%      $18,491,408      $1,163,311,909
96         Curve DAO Token\n \nCRV\n \nCRV      $2.93   0.5%   4.8%   15.7%     $192,400,021      $1,153,828,424
97    Magic Internet Money\n \nMIM\n \nMIM      $1.01   0.2%  -0.4%    0.5%      $46,752,764      $1,147,279,681
98               Ravencoin\n \nRVN\n \nRVN  $0.112977   0.3%  -0.4%    6.5%      $51,200,119      $1,109,215,081
99  Decentralized Social\n \nDESO\n \nDESO    $105.29  -1.3%  -6.7%  -33.3%         $275,178      $1,108,886,218

[100 rows x 7 columns]


'''


















