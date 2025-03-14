import requests,os,time
import numpy as np


def check_year_list(year_list):

    rest_year = np.arange(1982, 2021)
    total_year = [1977, 1980] + list(rest_year)
    year_index = -1

    for i in year_list:

        if i in total_year:
            year_index = 1
        else:
            year_index = 0
            print('[ year ' + str(i) + ' ]' + "'s data is not available right now.")
            break
    return year_index



def pre_download(this_year,next_year):

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    url_to_do = 'https://www.boxofficemojo.com/daily/' + str(this_year) + '/?view=year'
    html_name = 'year ' + str(this_year)
    next_file = 'year ' + str(next_year)
    page_download(url_to_do, headers, html_name, next_file)



def last_page_pre_download(this_year):

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    url_to_do = 'https://www.boxofficemojo.com/daily/' + str(this_year) + '/?view=year'
    html_name = 'year ' + str(this_year)
    next_file = 'year ' + str(this_year)
    page_download(url_to_do, headers, html_name, next_file)



def page_download(url_to_do,headers,html_name,next_file):

        url = url_to_do
        file_name = html_name

        if not os.path.exists('box_office_pages/' + file_name + '.html'):
            f = open('box_office_pages/'+ file_name + '.html.temp','w',encoding = 'utf-8')
            r = requests.get(url, headers=headers)
            r.encoding = r.apparent_encoding
            html = r.text
            f.write(html)
            f.close()
            os.rename('box_office_pages/'+ file_name + '.html.temp','box_office_pages/'+ file_name + '.html')
            print("\nFinish downloading page: " + '[ ' + file_name + ' ]')

            sleep_time = np.random.randint(5, 10) + np.random.normal(5, 2)

            if file_name != next_file:
                print('\nStart downloading page ' + '[ ' + next_file + ' ]' + ' in ' + str(sleep_time) + ' seconds...\n\n')
                time.sleep(sleep_time)
            else:
                pass
        else:
            print('File ' + '[ ' + file_name + ' ]' + ' has already been existed...')



def web_scrapping(year_list):

    assert type(year_list) is list, \
        "the 'year_list' must be a 'list'."

    if check_year_list(year_list) == 1:

        s_t = time.time()

        if not os.path.exists('box_office_pages'):
            os.mkdir('box_office_pages')

        for i in range(len(year_list)):
            if i != len(year_list) - 1:
                this_year = year_list[i]
                next_year = year_list[i + 1]
                pre_download(this_year,next_year)
            else:
                this_year = year_list[i]
                last_page_pre_download(this_year)

        e_t = time.time()
        total_time = e_t - s_t
        print('\n\nMission Complete \n\nTime Consuming:  ',total_time)




if __name__ == "__main__":

    #year_list = [i for i in range(2014,2021)]
    year_list = [2020]
    web_scrapping(year_list)
