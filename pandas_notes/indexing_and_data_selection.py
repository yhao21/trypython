import pandas as pd
import numpy as np



""""
loc and iloc:

    .loc is label based
    .iloc is integer position based

"""

a = pd.Series([1,3,5,7])
b = pd.Series([10,30,50,70])
c = pd.DataFrame([a,b])
d = pd.Series([1,5,2,2])
c = c.append(d,ignore_index = True)
c.columns = ['edu','exp','ab','age']
# print(c)

result = c.loc[:, ['edu','ab']]
# print(result)
"""
c
   edu  exp  ab  age
0    1    3   5    7
1   10   30  50   70
2    1    5   2    2

result
   edu  ab
0    1   5
1   10  50
2    1   2

"""


"""
column exchange:

this method will exchange the value under exp and edu, but the column name will not change.
"""
c.loc[:,['edu','exp']] = c[['exp','edu']].to_numpy()
print(c)

"""
   edu  exp  ab  age
0    3    1   5    7
1   30   10  50   70
2    5    1   2    2
"""
