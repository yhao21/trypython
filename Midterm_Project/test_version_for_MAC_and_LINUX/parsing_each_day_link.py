import pandas as pd
from bs4 import BeautifulSoup
import glob,os,math,time


def left_time_estimation(round_time,remain_workload):
    left_time = remain_workload * round_time
    if  left_time < 3600:
        time_estimation = str(math.modf(left_time/60)[1])
        seconds = str(round(math.modf(math.modf(left_time/60)[0])[0]*60,3))
        print('\nThis parsing section will be finished in [ ' + time_estimation + ' ] minutes [ ' + seconds + ' ] seconds...(2/6)')
    elif left_time >= 3600 and left_time < 86400:
        time_estimation = str(math.modf(left_time/60/60)[1])
        mins = str(math.modf(math.modf(left_time/60/60)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(left_time/60/60)[0]*60)[0]*60,2))
        print('\nThis parsing section will be finished in [ ' + time_estimation + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...(2/6)')
    elif left_time >= 86400 and left_time < 172800:
        time_estimation = str(math.modf(left_time/60/60/24)[1])
        hours = str(math.modf(math.modf(left_time/60/60/24)[0]*24)[1])
        mins = str(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[0]*60,2))
        print('\nThis parsing section will be finished in [ ' + time_estimation + ' ] day ' + '[ ' + hours + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...(2/6)')
    elif left_time >= 172800:
        time_estimation = str(math.modf(left_time/60/60/24)[1])
        hours = str(math.modf(math.modf(left_time/60/60/24)[0]*24)[1])
        mins = str(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[0]*60,2))
        print('\nThis parsing section will be finished in [ ' + time_estimation + ' ] days ' + '[ ' + hours + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...(2/6)')


def parsing_each_day_link():

    assert str(os.listdir('box_office_pages')) != '[]', \
        "You should download each year's page first!\n\nCheck if you have run [ web_scrapping.py ]"

    link_data = pd.DataFrame()

    for one_file in glob.glob('box_office_pages/*.html'):
        loads = [file for file in glob.glob('box_office_pages/*.html')]
        position = loads.index(one_file)
        remain_workload = len(loads) - position
        round_s_time = time.time()

        f = open(one_file,'r',encoding = 'utf-8')
        html = f.read()
        f.close()
        soup = BeautifulSoup(html,'html.parser')
        tds = soup.find_all('td', class_='a-text-left mojo-header-column mojo-truncate mojo-field-type-date_interval mojo-sort-column')
        for item in tds:
            date_link = item.find('a').get('href')
            full_link = 'https://www.boxofficemojo.com/' + date_link
            date = item.find('a').get_text()
            link_data = link_data.append({
                'Dates':date,
                'Links':full_link
            },ignore_index = True)

        round_e_time = time.time()
        round_time = round_e_time - round_s_time
        left_time_estimation(round_time, remain_workload=remain_workload)

    order = ['Dates','Links']
    link_data = link_data[order]
    print(link_data)
    link_data.to_csv('date_links.csv')


if __name__ == "__main__":

    parsing_each_day_link()