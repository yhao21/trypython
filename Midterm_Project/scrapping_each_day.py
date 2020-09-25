import os,requests,time,re
import pandas as pd
import numpy as np




def import_date_links():

    assert os.path.exists('date_links.csv') is True, \
        'You should get [ date_links.csv ] first.\nCheck if you have run [ web_scrapping.py ] and [ parsing_each_day_link.py ]'

    if not os.path.exists('Each_Day_Info'):
        os.mkdir('Each_Day_Info')

    links = pd.read_csv('date_links.csv')
    return links


def pre_download(day_links):

    links = day_links.iloc[:,2].values
    file_names = []

    for link in links:
        name = str(re.compile(r'.*date/(.*?)/\?ref.*').findall(link)).replace("['",'').replace("']",'')
        file_names.append(name)

    for date_order in range(len(file_names)):
        if date_order != len(file_names)-1:
            file_name = file_names[date_order]
            next_file = file_names[date_order+1]
            link = links[date_order]
            if not os.path.exists('Each_Day_Info/' + file_name + '.html'):
                download_date_link_info(file_name,link,next_file)
            else:
                print('File ' + '[ ' + file_name + ' ]' + ' has already been existed...')
        if date_order == len(file_names)-1:
            file_name = file_names[date_order]
            next_file = file_name
            link = links[date_order]
            if not os.path.exists('Each_Day_Info/' + file_name + '.html'):
                download_date_link_info(file_name, link, next_file)
            else:
                print('File ' + '[ ' + file_name + ' ]' + ' has already been existed...')



def download_date_link_info(file_name,link,next_file):

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    url = link

    r = requests.get(url,headers = headers)
    r.encoding = r.apparent_encoding
    html = r.text
    f = open('Each_Day_Info/' + file_name + '.html.temp','w',encoding = 'utf-8')
    f.write(html)
    f.close()
    os.rename('Each_Day_Info/' + file_name + '.html.temp','Each_Day_Info/' + file_name + '.html')
    print("\nFinish downloading page: " + '[ ' + file_name + ' ]')

    if file_name != next_file:
        sleep_time = np.random.randint(5, 10) + np.random.normal(5, 2)
        print('\nStart downloading page ' + '[ ' + next_file + ' ]' + ' in ' + str(sleep_time) + ' seconds...\n\n')
        time.sleep(sleep_time)
    else:
        pass




def scrapping_each_day():

    s_t = time.time()
    day_links = import_date_links()
    ##head for test
    # day_links = day_links.head()
    pre_download(day_links)
    e_t = time.time()
    total_time = e_t - s_t
    print('\n\nMission Complete \n\nTime Consuming:  ', total_time)




if __name__ == "__main__":

    scrapping_each_day()