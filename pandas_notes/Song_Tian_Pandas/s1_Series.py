import pandas as pd

# 生成一个20行的series
d = pd.Series(range(5))
print(d)
"""
0    0
1    1
2    2
3    3
4    4
dtype: int64
"""


"""对d进行前n项累加"""
print(d.cumsum())
"""
0     0
1     1
2     3
3     6
4    10
dtype: int64
"""