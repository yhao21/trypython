import numpy as np
import pandas as pd


movie_detal = pd.read_csv('movie_detail_info.csv')
every_day = pd.read_csv('every_day_movies.csv')

mov_col = [i for i in movie_detal.columns]
ev_col = [i for i in every_day.columns]
mov_col[0] = 'Index'

mov = movie_detal.iloc[:,:].values
ev = every_day.iloc[:5,:].values
a = np.hstack((ev,mov))


new = pd.DataFrame(a)
new.columns = ev_col+mov_col
new.pop('Unnamed: 0')
new.pop('Movie Name1')
new.pop('Date1')
new.pop('Index')


print(new)
new.to_csv('111.csv')

