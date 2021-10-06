import requests
import os
import pandas as pd
from tld import get_tld,get_fld
"""
如果你的url前面有很奇怪的域名，比如m.baidu.com,   alert.lll.com

如何整理这些不规律的url域名
需要一个package： tld
"""

if not os.path.exists('domain_html_file'):
    os.mkdir('domain_html_file')

df = pd.read_csv('domains.csv')
for link in df['1001coques.fr']:
    #注意，使用get_fld以后一定要加'http://'
    new_link = get_fld('http://' + link)
    url = 'http://www.' + new_link
    r = requests.get(url)
    print('success ' + link)



