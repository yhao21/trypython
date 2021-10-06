import os,requests,time,glob
import pandas as pd
import numpy as np



def import_date_links():

    assert os.path.exists('movie_links.csv') is True, \
        'You should get [ movie_links.csv ] first.\nCheck if you have run [ parsing_each_day.py ]'

    if not os.path.exists('Each_Movie_Info'):
        os.mkdir('Each_Movie_Info')

    links = pd.read_csv('movie_links.csv')
    return links



def pre_download(movie_link):

    links = movie_link.iloc[:, 3].values
    file_names = movie_link.iloc[:,2].values
    dates = movie_link.iloc[:,1].values

    for movie_order in range(len(file_names)):
        if movie_order != len(file_names)-1:
            file_name = str(movie_order) + '_' + str(dates[movie_order]) + '_' + file_names[movie_order]
            next_file = str(movie_order+1) + '_' + str(dates[movie_order]) + '_' + file_names[movie_order+1]
            link = links[movie_order]
            if not os.path.exists('Each_Movie_Info/' + file_name + '.html'):
                download_movie_info(file_name,link,next_file)
            else:
                print('File ' + '[ ' + file_name + ' ]' + ' has already been existed...')
        if movie_order == len(file_names)-1:
            file_name = str(movie_order) + '_' + str(dates[movie_order]) + '_' + file_names[movie_order]
            next_file = file_name
            link = links[movie_order]
            if not os.path.exists('Each_Movie_Info/' + file_name + '.html'):
                download_movie_info(file_name, link, next_file)
            else:
                print('File ' + '[ ' + file_name + ' ]' + ' has already been existed...')


def download_movie_info(file_name, link, next_file):

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    url = link

    r = requests.get(url, headers=headers,verify = False)
    r.encoding = r.apparent_encoding
    html = r.text
    f = open('Each_Movie_Info/' + file_name + '.html.temp', 'w', encoding='utf-8')
    f.write(html)
    f.close()
    os.rename('Each_Movie_Info/' + file_name + '.html.temp', 'Each_Movie_Info/' + file_name + '.html')
    print("\nFinish downloading page: " + '[ ' + file_name + ' ]')

    if file_name != next_file:
        sleep_time = np.random.randint(5, 10) + np.random.normal(5, 2)
        print('\nStart downloading page ' + '[ ' + next_file + ' ]' + ' in ' + str(sleep_time) + ' seconds...\n\n')
        time.sleep(sleep_time)
    else:
        pass



def scrapping_each_movie():

    s_t = time.time()
    movie_link = import_date_links()
    ##head for test
    # movie_link = movie_link.head()
    pre_download(movie_link)
    e_t = time.time()
    total_time = e_t - s_t
    print('\n\nMission Complete \n\nTime Consuming:  ', total_time)



if __name__ == "__main__":

    scrapping_each_movie()