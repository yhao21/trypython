import web_scrapping,parsing_each_day_link,scrapping_each_day,parsing_each_day,scrapping_each_movie,parsing_each_movie
import pandas as pd
import numpy as np
import math,time


def time_consumption(total_time):
    left_time = total_time
    if  left_time < 3600:
        time_estimation = str(math.modf(left_time/60)[1])
        seconds = str(round(math.modf(math.modf(left_time/60)[0])[0]*60,3))
        print('\nThis project costs you [ ' + time_estimation + ' ] minutes [ ' + seconds + ' ] seconds...')
    elif left_time >= 3600 and left_time < 86400:
        time_estimation = str(math.modf(left_time/60/60)[1])
        mins = str(math.modf(math.modf(left_time/60/60)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(left_time/60/60)[0]*60)[0]*60,2))
        print('\nThis project costs you [ ' + time_estimation + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...')
    elif left_time >= 86400 and left_time < 172800:
        time_estimation = str(math.modf(left_time/60/60/24)[1])
        hours = str(math.modf(math.modf(left_time/60/60/24)[0]*24)[1])
        mins = str(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[0]*60,2))
        print('\nThis project costs you [ ' + time_estimation + ' ] day ' + '[ ' + hours + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...')
    elif left_time >= 172800:
        time_estimation = str(math.modf(left_time/60/60/24)[1])
        hours = str(math.modf(math.modf(left_time/60/60/24)[0]*24)[1])
        mins = str(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[1])
        seconds = str(round(math.modf(math.modf(math.modf(left_time/60/60/24)[0]*24)[0]*60)[0]*60,2))
        print('\nThis project costs you [ ' + time_estimation + ' ] days ' + '[ ' + hours + ' ] hours [ ' + mins + ' ] minutes [ ' + seconds + ' ] seconds...')






year_list = [2014]

s_t = time.time()
web_scrapping.web_scrapping(year_list)
parsing_each_day_link.parsing_each_day_link()
scrapping_each_day.scrapping_each_day()
parsing_each_day.parsing_each_day()
scrapping_each_movie.scrapping_each_movie()
parsing_each_movie.parsing_each_movie()

print('\n\nWe are almost there.....\n\n')

df1 = pd.DataFrame(pd.read_csv('every_day_movies.csv')).sort_values(by = 'Movie Name')
df2 = pd.DataFrame(pd.read_csv('movie_detail_info.csv')).sort_values(by = 'Movie Name1')
df1_val = df1.iloc[:len(df2),:].values
df2_val = df2.iloc[:,:].values
df1_col = [i for i in df1.columns]
df2_col = [j for j in df2.columns]
df = pd.DataFrame(np.hstack((df1_val,df2_val)))
df.columns = df1_col + df2_col
df.pop('Unnamed: 0')
df.pop('Movie Name1')
df.replace('[]','No Information',inplace = True)
df['Number Of Days In Release'].replace('-','No Information',inplace = True)
df.to_csv('Box_Office_Info_Merge.csv')
print(df)

e_t = time.time()
total_time = e_t - s_t
time_consumption(total_time)

print('Done! Thanks for using my program! See you next time....^.^ ')