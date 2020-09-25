import web_scrapping,parsing_each_day_link,scrapping_each_day,parsing_each_day,scrapping_each_movie,parsing_each_movie
import pandas as pd
import numpy as np
import time


year_list = [i for i in range(2014,2021)]

start_time = time.time()

web_scrapping.web_scrapping(year_list)
parsing_each_day_link.parsing_each_day_link()
scrapping_each_day.scrapping_each_day()
parsing_each_day.parsing_each_day()
scrapping_each_movie.scrapping_each_movie()
parsing_each_movie.parsing_each_movie()


movie_detal = pd.read_csv('movie_detail_info.csv')
every_day = pd.read_csv('every_day_movies.csv')
mov_col = [i for i in movie_detal.columns]
ev_col = [i for i in every_day.columns]
mov_col[0] = 'Index'

mov = movie_detal.iloc[:,:].values
ev = every_day.iloc[:,:].values
a = np.hstack((ev,mov))
new = pd.DataFrame(a)
new.columns = ev_col + mov_col
new.pop('Unnamed: 0')
new.pop('Movie Name1')
new.pop('Date1')
new.pop('Index')


print(new)
new.to_csv('Box Office Info Merge.csv')

# end_time = time.time()
# total_time = end_time - start_time
# print('\n\nMission Complete \n\nTime Consuming:  ',total_time)