import pandas as pd
import numpy as np
from sklearn import linear_model



"""
every regression is a dimension reduction process


supervised learning:
    if data is discrete: called classification
    if data is continuous: called regression
    
unsupervised learning:
    if data is discrete: clustering
    if data is continuous: association
    
在终端中输入head -n + csvfile, 你可以看到前n个数据
head命令不会把文件中所有的数据load出来，他只会把你输入的行数对一个的数据读取出来，所以很快

如何获取subset of the data set by using head command
head -1000 ols.csv > "new file name"
then you can open it in excel or whatever app you want



index is the identification of each row

id means a lot:
    each row represents an individual, they have own individual id
    for each household, it may consists by many individuals. thus, several individuals can have same household id, while their individual ids are different.
     

"""


df = pd.read_csv('ols_dataset.csv')

#在pandas下面print与python的print的是不一样的。pandas重写了print函数
print(df)
"""
pandas 和 sklearn非常不和谐。。。。如果你的dataset使用pandas导入，有一定机率不能用

how to trans pandas dataframe into sth sklearn can read for sure:


target = df.iloc[:,2]

[row,col] so, [:,2] = second col of all rows

add .values    you can trans into array


NOTICE: sklearn doesn't accept missing data. you have to make sure you have a clean dataset

"""

target = df.iloc[:,2].values
print(target)
"""[2904.5 1706.7 3083.5 ... 4319.5 5159.  4131.2]"""

#把所有x（i）导入
data = df.iloc[:,3:10].values
print(data)


regression = linear_model.LinearRegression()

regression.fit(data,target)







