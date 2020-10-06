import os, time
import pandas as pd
import urllib.request
import requests
import re



if not os.path.exists('deep_link_html'):
    os.mkdir('deep_link_html')



df = pd.read_csv('coin_csv.csv')
#print(df.columns)






for link in df['link']:
    
    url = str(link)
    #print(url)
    file_name = re.compile(r'currencies/(\w*)').findall(url)[0]
    #print(file_name)

    if os.path.exists('deep_link_html/' + file_name + '.html'):
        print('file exists: ' + file_name + '.html')
        time.sleep(1)

    else:
        print('download: ' + file_name + '.html')

        r = requests.get(url)
        html = r.text

        f = open('deep_link_html/' + file_name + '.html.temp', 'w')
        f.write(html)
        f.close()
        os.rename('deep_link_html/' + file_name + '.html.temp', 'deep_link_html/' \
                + file_name + '.html')

        

        time.sleep(1)

