import pandas as pd
from pathlib import Path
import os





# Load data
path_data = Path.cwd()/'data'/'dataset_ps_4.csv'
df = pd.read_csv(path_data)


# ~~~~~~~~~~~~~~~~~~~~~
# df.query()
# ~~~~~~~~~~~~~~~~~~~~~
###------query manually------###
"""
Example of data:
         id  earnings  occ  ability  age  region  female  education  exp
0         1   1540.75    1       30   39       1       0          4   32
1         2   2282.25    3       71   34       1       0          8   25
2         3   3578.95   18       83   47       1       1         11   32

Suppose I want to get obs that occ == 3 and age == 35
"""
# Traditional way:
df_old = df[(df['occ'] == 3) & (df['age'] == 35)]
# Or
df_old = df.loc[(df['occ'] == 3) & (df['age'] == 35)]

"""
An easier way to do it is to use df.query()
"""
df_new = df.query("occ == 3 and age == 35")
"""
You can also add more conditions, e.g., occ is 3, age is 35, and male.
It allows you to right your query in string in stead of dealing with bunch of [], &, | ...
"""
df_new = df.query("occ == 3 and age == 35 and female == 0")
"""
Consider this short df named df1

   id  earnings  occ  ability  age  region  female  education  exp
0   1   1540.75    1       30   39       1       0          4   32 * +
1   2   2282.25    3       71   34       1       0          8   25   +
2   3   3578.95   18       83   47       1       1         11   32 
3   4   3023.50   21       50   45       2       0          7   37 
4   5   4608.95   25       92   41       1       1         11   28 
5   6   4164.00   34       62   46       4       0          8   34 
6   7   3399.75   26       20   30       1       0          2   26 
7   8   4324.95   22       99   43       3       1         15   22 
8   9   3175.70   12       38   45       4       1          5   35 
9  10   3681.00   22       52   46       2       0          5   38 *

I want male, and based on that edu can be either 4 or 5 (rows with *)
"""
df1 = df.head(10)
df_new = df1.query("female == 0 and (education == 4 or education == 5)")
"""
If I want occ < 20 and male (rows with +)
"""
df_new = df1.query("occ < 20 and female == 0")


###------Use values of another variable------###
"""
Define a new variable: age_condition = 40, I can put that variable in df.query() using @.
For example, to get obs with age < age_condition
"""
age_condition = 40
df_new = df1.query("age < @age_condition")

###------select rows with its column value is in a list------###
"""
   id  earnings  occ  ability  age  region  female  education  exp
0   1   1540.75    1       30   39       1       0          4   32
1   2   2282.25    3       71   34       1       0          8   25 *
2   3   3578.95   18       83   47       1       1         11   32 *
3   4   3023.50   21       50   45       2       0          7   37
4   5   4608.95   25       92   41       1       1         11   28 *
5   6   4164.00   34       62   46       4       0          8   34 *
6   7   3399.75   26       20   30       1       0          2   26
7   8   4324.95   22       99   43       3       1         15   22
8   9   3175.70   12       38   45       4       1          5   35
9  10   3681.00   22       52   46       2       0          5   38

Suppose I want to select rows in which education is 11, 8
"""
df_new = df1.query("education in [8, 11]")

"""
If I want to select rows that its value in region is not equal to 2 or 3
"""
# previously I should use ~ to refer the inverse result
df_new = df1[~df1['region'].isin([2,3])]
# A more readable way to do it is through
df_new = df1.query("region not in [2, 3]")






print(df_new)
