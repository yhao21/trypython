import pandas as pd
from bs4 import BeautifulSoup
import os,glob,re,time,math


def left_time_estimation(round_time,remain_workload):
    left_time = remain_workload * round_time
    if  left_time < 3600:
        time_estimation = str(math.modf(left_time/60)[1])
        seconds = str(round(math.modf(math.modf(left_time/60)[0])[0]*60,3))
        print('\nThis parsing section will be finished in [ ' + time_estimation + ' ] minutes [ ' + seconds + ' ] seconds...(4/6)')
    elif left_time >= 3600 and left_time < 86400:
        time_estimation = str(math.modf(left_time/60/60)[1])
        mins = str(math.modf(math.modf(left_time/60/60)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(left_time/60/60)[0]*60)[0]*60,2))
        print('\nThis parsing section will be finished in [ ' + time_estimation + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...(4/6)')
    elif left_time >= 86400 and left_time < 172800:
        time_estimation = str(math.modf(left_time/60/60/24)[1])
        hours = str(math.modf(math.modf(left_time/60/60/24)[0]*24)[1])
        mins = str(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[0]*60,2))
        print('\nThis parsing section will be finished in [ ' + time_estimation + ' ] day ' + '[ ' + hours + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...(4/6)')
    elif left_time >= 172800:
        time_estimation = str(math.modf(left_time/60/60/24)[1])
        hours = str(math.modf(math.modf(left_time/60/60/24)[0]*24)[1])
        mins = str(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[0]*60,2))
        print('\nThis parsing section will be finished in [ ' + time_estimation + ' ] days ' + '[ ' + hours + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...(4/6)')


def parsing_each_day():

    assert str(os.listdir('Each_Day_Info')) != '[]', \
        "You should download each day's page first!\n\nCheck if you have run [ scrapping_each_day.py ]"

    daily_movies = pd.DataFrame()
    movie_links = pd.DataFrame()

    for one_file in glob.glob('Each_Day_Info/*.html'):
        loads = [file for file in glob.glob('Each_Day_Info/*.html')]
        position = loads.index(one_file)
        remain_workload = len(loads) - position
        round_s_time = time.time()

        f = open(one_file,'r',encoding = 'utf-8')
        html = f.read()
        f.close()
        soup = BeautifulSoup(html,'html.parser')
        try:
            rows = soup.find('table',class_ = 'a-bordered a-horizontal-stripes a-size-base a-span12 mojo-body-table mojo-table-annotated mojo-body-table-compact').find_all('tr')
            for items in rows:
                try:
                    tds = items.find_all('td')
                    if tds[2].string != None:
                        names = str(tds[2].string.replace(':','').replace('?','').replace('/','').replace('"',''))
                    else:
                        names = str(tds[2].find('a').string.replace(':','').replace('?','').replace('/','').replace('"',''))
                    if names not in daily_movies.values:
                        daily_gross = tds[3].string.replace('$','')
                        theaters = tds[6].string
                        gross_to_date = tds[8].string.replace('$','')
                        days_release = tds[9].string
                        distributers = str(re.compile(r'_blank">(.*?)<svg class=').findall(str(tds[10]))).replace("['",'').replace("']",'')
                        movie_link = 'https://www.boxofficemojo.com/' + tds[2].find('a').get('href')
                        dates = str(one_file).replace('Each_Day_Info\\','').replace('.html','')
                        daily_movies = daily_movies.append({
                            'Date':dates,
                            'Movie Name':names,
                            'Daily Box Office':daily_gross,
                            'Theaters':theaters,
                            'Gross Box Office To Date':gross_to_date,
                            'Number Of Days In Release':days_release,
                            'Distributer':distributers
                        },ignore_index = True)

                        movie_links = movie_links.append({
                            'Date': dates,
                            'Movie Name':names,
                            'Movie Link':movie_link
                        },ignore_index = True)
                    else:
                        pass
                except:
                    pass
        except:
            pass

        round_e_time = time.time()
        round_time = round_e_time - round_s_time
        left_time_estimation(round_time, remain_workload=remain_workload)

    order = ['Movie Name','Date','Daily Box Office','Theaters','Gross Box Office To Date','Number Of Days In Release','Distributer']
    daily_movies = daily_movies[order]
    print(daily_movies)
    daily_movies.to_csv('every_day_movies.csv')

    order_links = ['Movie Name','Date','Movie Link']
    movie_links = movie_links[order_links]
    movie_links.to_csv('movie_links.csv')
    print(movie_links)


if __name__ == "__main__":

    parsing_each_day()


