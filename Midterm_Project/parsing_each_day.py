import pandas as pd
from bs4 import BeautifulSoup
import os,glob,re



def parsing_each_day():

    assert str(os.listdir('Each_Day_Info')) != '[]', \
        "You should download each day's page first!\n\nCheck if you have run [ scrapping_each_day.py ]"

    daily_movies = pd.DataFrame()
    movie_links = pd.DataFrame()
    for one_file in glob.glob('Each_Day_Info/*.html'):
        f = open(one_file,'r',encoding = 'utf-8')
        html = f.read()
        soup = BeautifulSoup(html,'html.parser')
        try:
            rows = soup.find('table',class_ = 'a-bordered a-horizontal-stripes a-size-base a-span12 mojo-body-table mojo-table-annotated mojo-body-table-compact').find_all('tr')
            for items in rows:
                try:
                    tds = items.find_all('td')
                    if tds[2].string != None:
                        names = str(tds[2].string.replace(':',''))
                    else:
                        names = str(tds[2].find('a').string.replace(':',''))

                    daily_gross = tds[3].string.replace('$','')
                    theaters = tds[6].string
                    gross_to_date = tds[8].string.replace('$','')
                    days_release = tds[9].string
                    distributers = str(re.compile(r'_blank">(.*?)<svg class=').findall(str(tds[10]))).replace("['",'').replace("']",'')
                    movie_link = 'https://www.boxofficemojo.com/' + tds[2].find('a').get('href')
                    dates = str(one_file).replace('Each_Day_Info/','').replace('.html','')
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
                except:
                    pass
        except:
            pass
    order = ['Date','Movie Name','Daily Box Office','Theaters','Gross Box Office To Date','Number Of Days In Release','Distributer']
    daily_movies = daily_movies[order]
    print(daily_movies)
    daily_movies.to_csv('every_day_movies.csv')

    order_links = ['Date','Movie Name','Movie Link']
    movie_links = movie_links[order_links]
    movie_links.to_csv('movie_links.csv')
    print(movie_links)


if __name__ == "__main__":

    parsing_each_day()


