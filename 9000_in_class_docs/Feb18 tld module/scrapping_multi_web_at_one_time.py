import os
import glob
import pandas as pd
import requests


if not os.path.exists('domain_html_file'):
    os.mkdir('domain_html_file')


"""注意，一定要规定不要列标题，不然会把第一个值当做标题"""
#为什么第一个值变成了标题
df = pd.read_csv('domains.csv')
# print(df)
#方括号里是列名
for link in df['1001coques.fr']:
    file_name = link
    link = 'http://' + link
    print(link)
    f = open('domain_html_file/' + file_name + '.html', 'w',encoding="utf-8")
    r = requests.get(link)
    html = r.text
    f.write(html)
    f.close()
