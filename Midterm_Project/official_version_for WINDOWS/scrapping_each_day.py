import os,requests,time,re,math
import pandas as pd
import numpy as np



def left_time_estimation(round_time,sleep_time,remain_workload):
    left_time = remain_workload * (round_time + sleep_time)
    if  left_time < 3600:
        time_estimation = str(math.modf(left_time/60)[1])
        seconds = str(round(math.modf(math.modf(left_time/60)[0])[0]*60,3))
        print('\nThis scrapping section will be finished in [ ' + time_estimation + ' ] minutes [ ' + seconds + ' ] seconds...(3/6)')
    elif left_time >= 3600 and left_time < 86400:
        time_estimation = str(math.modf(left_time/60/60)[1])
        mins = str(math.modf(math.modf(left_time/60/60)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(left_time/60/60)[0]*60)[0]*60,2))
        print('\nThis scrapping section will be finished in [ ' + time_estimation + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...(3/6)')
    elif left_time >= 86400 and left_time < 172800:
        time_estimation = str(math.modf(left_time/60/60/24)[1])
        hours = str(math.modf(math.modf(left_time/60/60/24)[0]*24)[1])
        mins = str(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[0]*60,2))
        print('\nThis scrapping section will be finished in [ ' + time_estimation + ' ] day ' + '[ ' + hours + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...(3/6)')
    elif left_time >= 172800:
        time_estimation = str(math.modf(left_time/60/60/24)[1])
        hours = str(math.modf(math.modf(left_time/60/60/24)[0]*24)[1])
        mins = str(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[0]*60,2))
        print('\nThis scrapping section will be finished in [ ' + time_estimation + ' ] days ' + '[ ' + hours + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...(3/6)')



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
            remain_work = len(file_names) - date_order - 1
            if not os.path.exists('Each_Day_Info/' + file_name + '.html'):
                download_date_link_info(file_name,link,next_file,remain_workload = remain_work)
            else:
                print('File ' + '[ ' + file_name + ' ]' + ' has already been existed...')
        if date_order == len(file_names)-1:
            file_name = file_names[date_order]
            next_file = file_name
            link = links[date_order]
            remain_work = len(file_names) - date_order - 1
            if not os.path.exists('Each_Day_Info/' + file_name + '.html'):
                download_date_link_info(file_name, link, next_file,remain_workload = remain_work)

            else:
                print('File ' + '[ ' + file_name + ' ]' + ' has already been existed...')



def download_date_link_info(file_name,link,next_file,remain_workload):

    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}
    url = link
    round_s_time = time.time()

    r = requests.get(url,headers = headers)
    r.encoding = r.apparent_encoding
    html = r.text
    f = open('Each_Day_Info/' + file_name + '.html.temp','w',encoding = 'utf-8')
    f.write(html)
    f.close()
    os.rename('Each_Day_Info/' + file_name + '.html.temp','Each_Day_Info/' + file_name + '.html')
    print("\nFinish downloading page: " + '[ ' + file_name + ' ]')

    round_e_time = time.time()
    round_time = round_e_time - round_s_time
    sleep_time = np.random.randint(5, 10) + np.random.normal(5, 2)
    left_time_estimation(round_time, sleep_time, remain_workload=remain_workload)

    if file_name != next_file:

        print('\nStart downloading page ' + '[ ' + next_file + ' ]' + ' in ' + str(sleep_time) + ' seconds...\n\n')
        time.sleep(sleep_time)
    else:
        pass




def scrapping_each_day():

    s_t = time.time()
    day_links = import_date_links()
    pre_download(day_links)
    e_t = time.time()
    total_time = e_t - s_t
    print('\n\nSection Complete \n\nTime Consuming:  ', total_time)




if __name__ == "__main__":

    scrapping_each_day()