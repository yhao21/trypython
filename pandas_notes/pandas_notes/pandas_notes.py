import pandas as pd
import re


df = pd.read_csv('sample_data.csv')
"""
1. load csv file
    df = pd.read_csv('sample_data.csv')



2. print head or particlular rows, n can be any number
it will print n rows
if n is a negative number, i.e. -3, it will print all rows
except the last three rows

    print(df.head(n))



3. print column names or title of each columns
    print(df.columns)



4. print a single column's data
    print(df['columns name']) 
    print(df['Severity'])

    or 
    
    print(df.columns name)
    print(df.State)



5. print multiple columns data
    print(df[['col1 name','col2 name', 'col3 name']])
    print(df[['Severity','State']])



6. print specific row and column
    if you want to print row 1-3
    print(df.iloc[1:4,:])

    NB: index befre ',' indicate which row(s) you want to print,
        in this example, 1:4 means print from 2nd(line 1) to 4th(line 3) row.
        remember, python start from row #0

    if you want to print row 1-3 with columns 1-3
    print(df.iloc[1:4, 1:4])

6.1 find a row using row index
    

    Row example:
            YYYYMM    ID IDPREV  DATEPR IndividualID
    313937  202309  2101   1082  202303         null

    Suppose you want to find this row, and the row index is 313937, you can choose:
    1. df.loc[313937], which will return a serie.
    2. df.loc[[313937]], which will return a df.




7. print specific cell
    if you want to print the value in the first row and second column
        print(df.iloc[0,1])



8. print a column with index:
    for index, row in df.iterrows():
        print(index, row['column name'])


    i.e.
    for index, row in df.iterrows():
        print(index, row['ID'])



9. print all rows with "specific value in a columns"
    suppose I want to know the rows with 'Severity' == 3 (remember, severity
    is a column)
        print(df.loc[df['Severity'] == 3])

    Notice, iloc is used to deal with numarica index, while loc is for string



10. print rows satisfy multiple conditions in columns value
    df.loc[(<condition 1>) & (<condition 2>) & (<condition 3>)....]
    & 表示只有所有条件均符合才能被print出来。
    i.e, 
        a = df.loc[(df['Severity'] == 3) & (df['TMC'] == 201.0) & (df['Sunrise_Sunset'] == 'Day')]
        print(a)

    如果想要列出severity == 3 或者 TMC == 201.0的则可以将 & 替换为 |   

    如果想筛选出某一列中值为a或者为b的行，可以如下操作：
    这里我们要借助正则表达式  regular expression

    import re

    df.loc['Severity']

11. print the description of the data set
    it contains 'count', 'mean', 'std', 'min', 'max', ... for each column
        print(df.describe())

    if you want the description for a particular column:
        print(df.describe()['column name'])
        i.e.
        print(df.describe()['Severity'])

    if you want the description for multiple columns:
        print(df.describe()[['Severity', 'TMC']])



12. 数据排序
    df.sort_values('columns name')
    会按照该列数据从小到大排序， 

    若想要从大到小排序：
    df.sort_values('columns name', ascending = False)

    若想按照多列数据排序， 
    df.sort_values(['col1', 'col2', 'col3']')
    程序会以col1大小进行排序，然后，对有相同值的行按照col2的大小进行排序，最后按照col3
    故， 优先级为 col1， col2， col3


    若想 先以col1大小进行正向排序，而后相同值的行按照col2大小进行 逆向 排序
    a = df.sort_values(['TMC', 'ID'], ascending = [1, 0])
    ascending中， 1表示true， 0表示false， 故， TMC以ascending方式排序
    ID以descending方式排序



    You can also sort by index:
        After you count frequency of each value in a column using 
            freq = df['col'].value_counts(),
        the series is sorted by frequency, instead of the index.

        You can use <series.sort_index()> to sort by index, i.e., 
            freq.sort_index()



13. 删除某一列
    df = df.drop(columns = ['<col name>'])
    要将删除后的df赋值给一个新的变量。 这里重新赋值给df等于替换掉了原有df。



14. 想要新建一列， 并让这一列的值为前面某几列的加总

    df['<new col name>'] = df.iloc[start row : end row, start col : end col].sum(axis = 1)
    axis = 1 表示每一行进行加总，程序会在行位对选中的列们进行加总，并将加总值创建为新的一列
    axis = 0 表示纵向加总，，相当于对某一列进行加总。

    比如我们想在每一行最后添加一个total， total = TMC + Severity 
        df['total'] = df.iloc[:, 3:5].sum(axis = 1)
    注意，TMC是第3列， Unname是第0列。Severity是第4列。 python中括号结尾的那一列是取不到的。
    所以要以5结尾。这样就是取3、4两列。

    另一个比较原始的方法就是：
        df['total'] = df['TMC'] + df['Severity']
       


15. 如果想要调整列的顺序， 比如想要前两列为 TMC 和 Severity

    col = list(df.columns)
    df = df[col[3:5] + col[:3] + col[5:]]

    3:5表示的就是TMC和Severity， 用加好把剩下的列排列起来



16. 保存dataframe为csv文件
    df.to_csv('five name/or path')
    这样保存后的csv，第一列是序号列。如果不想要需要：
    df.to_csv('file_name.csv', index = None)



17. 如果想显示某一列的字符串中包含 “特定字符内容” 的行：
    a = df.loc[df['Sunrise_Sunset'].str.contains('Day')]

    表示 显示sunrise这一列中字符串里包含Day这个单词的所有行


    如果向显示不包含 day 的行：
    a = df.loc[~df['Sunrise_Sunset'].str.contains('Day')]

    加上波浪线 ~ 即可


    Or:

    a = df[df['mktcap'].astype('str').str.contains('NIF')]


18. Delete row with NaN, delete empty line
    
    df = df.dropna()

18.1 Replace nan by '':
    df = df.replace(np.nan, '')

18.2 Replace values in multiple rows
    Replace 0 by 10 in column A and B
        df = df.replace({'A':{0:10}, 'B':{0:10}})
18.3 Replace multiple values in a same column.
    Replace 0 by 1, 2 by 5
        df = df.replace({'A':{0:1, 2:5}})


19. reset the index:

    df = df.reset_index(drop = True)


20. combine dataframe 合并dataframe
    水平合并
    pd.concat([df1, df2], axis = 1)
    垂直合并
    pd.concat([df1, df2], axis = 0)


21. Count Frequency 
    df_frequency = df['Crime Type'].value_counts()
    
    it will return a frequency for unique categories in this col
        HUMAN TRAFFICKING                        3
        PUBLIC INDECENCY                         3
        OTHER NARCOTIC VIOLATION                 2
        Name: Primary Type, dtype: int64


    To obtain the categories:
    df_frequency = df['Crime Type'].value_counts().index.tolist()
        you receive a list ['HUMAN TRAFFICKING','PUBLIC INDECENCY', ...]


22. list unique value in a column
    pd.unique(df['Crime Trype']))

    or

    self.df['hour'].unique()



23. plot the density of a series
    consider you have a log price series, lnprice you want to plot the
    density, then
        dens_series = pd.Series(lnprice)
        dens_series.plot.density()  # this will generate plt obj
        plt.show()

    more details see:
    https://pandas.pydata.org/pandas-docs/version/0.23/generated/pandas.Series.plot.density.html






24. change value for a particular cell:

    df.at[row_index, column_name] = value

    example:
    crypto_df.at[row_index, 'open_price'] = 1


    ## Or, to change the value which can be find following a certain condition:

    raw_df:
              col1 col2
            0    a    b
            1    c    d
    Want to change "d" to "2"

        a.loc[a['col1'] == 'c', ['col2']] = 2

              col1 col2
            0    a    b
            1    c    2



25. extract a particular value from df

    value = df.loc[[row_index]][column_name].values[0]




26. print rows contain values between a range

    For example, print beta (coef) between 0.99 and 1.01:

    df = pd.read_csv('csv_folder/capm_beta.csv')
    closely_to_mkt = df[df['coef'].between(0.99, 1.01)]


27. fill missing data with the mean of the entire dataset
(which is useless...)
data = data_df.copy()
data.fillna(data.mean(), inplace = True)

28 data imputation (missing data)
##Method 1: use KNN model

    from sklearn.impute import KNNImputer
    
    imputer = KNNImputer(n_neighbors = 2, weights = 'uniform')
    data3 = pd.DataFrame(imputer.fit_transform(df))
    data3.columns = df.columns
    
##Method 2: IterativeImputer
https://scikit-learn.org/stable/modules/generated/sklearn.impute.IterativeImputer.html
##Method 3: MissingIndicatorhttps://scikit-learn.org/stable/modules/generated/sklearn.impute.MissingIndicator.html



29 Standardization:

    Method 1: Box-Cox
    Method 2: Yeo-Johnson



30 groupby
    if you want to return a df, set as_index = False. Otherwise, it will return a Series

    Here "transfer" is a column name.

    df = df.groupby(['timestamp'], as_index=False).transfer.sum()



31 generate a list of date

    
    date_list = pd.date_range(start = '2015-08-07', end = '2022-09-30')



32 merge two column into a stacked one column


    Given a 3 by 2 dataframe, df:
    
       x  y
    0  1  2
    1  3  4
    2  5  6
    
    We can use <df.unstack()> to merge column x and y to a single stacked column below:
    
    0    1
    1    3
    2    5
    3    2
    4    4
    5    6
    
    
    Code:
    
            df = pd.DataFrame([[1,2],[3,4],[5,6]], columns = ['x', 'y'])
            df = df.unstack().reset_index(drop = True)
    
    
    
    **** <df.unstack() > will concat column "y" below column x ****
    


33 convert columns to datetime
    official documents: https://pandas.pydata.org/docs/reference/api/pandas.to_datetime.html



    You can also state the input format. For example, if the input is 202301, you can
    set the format as:
        
        df['YYYYMM'] = pd.to_datetime(df['YYYYMM'], format = "%Y%m")
        Result: 2023-09

    If you want to convert datetime to strings in particular format, you can set the 
    format you preferred by using
        df['YYYYMM'] = pd.to_datetime(df['YYYYMM'], format = "%Y%m").dt.strftime('%Y-%m')


    dataset['Date'] = pd.to_datetime(dataset['Date'])
    print(dataset['Date'])

    
    
    
    # extract year info from datetime
    dataset['year'] = dataset['Date'].dt.year
    # extract month info from datetime
    dataset['month'] = dataset['Date'].dt.month
    # extract hour info from datetime
    dataset['hour'] = dataset['Date'].dt.hour
    dataset['minute'] = dataset['Date'].dt.hour
    
    
    
    
    ## regroup hours to different groups, i.e., group 0 = 0 AM to 3 AM
    dataset['hour_slot'] = np.select([
        (dataset['hour'] < 4),
        (dataset['hour'] < 8),
        (dataset['hour'] < 12),
        (dataset['hour'] < 16),
        (dataset['hour'] < 20),
        (dataset['hour'] < 24),
        ],[0,1,2,3,4,5])
    
    
    
    dataset['minute_slot'] = np.select([
        (dataset['minute'] < 15),
        (dataset['minute'] < 30),
        (dataset['minute'] < 45),
        (dataset['minute'] < 60),
        ],[0,1,2,3])
    
    


34 Computes days, weeks, months, and years in df

    df['diff_days'] = (df['end_date'] - df['start_date']) / np.timedelta64(1, 'D')
    df['diff_weeks'] = (df['end_date'] - df['start_date']) / np.timedelta64(1, 'W')
    df['diff_months'] = (df['end_date'] - df['start_date']) / np.timedelta64(1, 'M')
    df['diff_years'] = (df['end_date'] - df['start_date']) / np.timedelta64(1, 'Y')
    
    #view updated DataFrame
    print(df)
    
      start_date   end_date  diff_days  diff_weeks  diff_months  diff_years
    0 2020-01-05 2020-06-30      177.0   25.285714     5.815314    0.484610
    1 2020-01-12 2020-07-31      201.0   28.714286     6.603832    0.550319
    2 2020-01-19 2020-08-31      225.0   32.142857     7.392349    0.616029
    3 2020-01-26 2020-09-30      248.0   35.428571     8.148011    0.679001
    4 2020-02-02 2020-10-31      272.0   38.857143     8.936528    0.744711
    5 2020-02-09 2020-11-30      295.0   42.142857     9.692191    0.807683







###------Math in dataframe------###

# create a df:

a =[
        [1,2,1],
        [1,2,2],
        [2,2,1],
        [2,2,1],
        ]

df = pd.DataFrame(a, columns = ['year', 'inf', 'wt'])
#          year  inf  wt
#       0     1    2   1
#       1     1    2   2
#       2     2    2   1
#       3     2    2   1

##------math of a column condition on the row values of another column------##
#Use groupby to group rows with same values. For example, if we want to sum the inflation
#rate for each year, we need to group rows according to values in 'year' col. Then sum()
#the values in 'inf' col for each group.

result = df.groupby(['year'])['inf'].sum()
print(result)
#       year
#       1    4
#       2    4

##------math between two cols condition on the row values of another column------##
# Suppose we want to multiply inf by wt then sum the product for each year, 

result = df.groupby(['year']).apply(lambda row: (row.inf * row.wt).sum())
print(result)

#       year
#       1    6          =2*1+2*2
#       2    4          =2*1+2*1

#we can further compute the weighted average, which is devide what we get above by the
#summation of weight in each year.

result = df.groupby(['year']).apply(lambda row: (row.inf * row.wt).sum()/row.wt.sum())
print(result)
#       year
#       1    2.0        =(2*1+2*2)/(1+2)
#       2    2.0        =(2*1+2*1)/(1+1)





###------Search------###
##------Find rows that are before a certain year------##

df = pd.read_csv('./dataset.csv')
df['YYYYMM'] = df['YYYYMM'].astype('datetime64')
a = df[df['YYYYMM'].apply(lambda x: x.year < 1979)]
print(a)






###------Count obs using groupby.size()------###

df_missing_frequency['num._of_obs'] = df_raw.groupby(time_col).size().values







###------Lag terms------###
To create a lag term of a column, we can use <shift> function


          YYYYMM  AGE  PX1_weighted  
0     1978-01-01   18      0.000000  
1     1978-01-01   19      1.462500  
2     1978-01-01   20      1.858700  
3     1978-01-01   21      2.323373  
4     1978-01-01   22      6.183000  


To create a lag term for PX1_weighted, 
    
    df['PX1_weighted_lag1'] = df['PX1_weighted'].shift(1)

where the numerical value in the parenthesis of the shift function identify the lag period. 


Result:

          YYYYMM  AGE  PX1_weighted    PX1_weighted_lag1
0     1978-01-01   18      0.000000                  NaN
1     1978-01-01   19      1.462500             0.000000
2     1978-01-01   20      1.858700             1.462500
3     1978-01-01   21      2.323373             1.858700
4     1978-01-01   22      6.183000             2.323373




###------Convert month to quarter------###

Suppose I have df below,

         YYYYMM  Inflation
0    1872-01-01   1.524880
1    1872-02-01  -1.479751
2    1872-03-01  -1.458173
3    1872-04-01   4.538217
4    1872-05-01   7.008965


I want to compute quarterly average inflation. 

    # convert YYYYMM to quarter
    df['YYYYMM'] = pd.PeriodIndex(pd.to_datetime(df.YYYYMM), freq = 'Q')

    # Then group by quarter and compute mean.
    df = df.groupby(['YYYYMM'], as_index = False).mean()
     YYYYMM  Inflation
0    1872Q1  -0.471015
1    1872Q2   6.470473
2    1872Q3   7.366998
3    1872Q4   3.836112
4    1873Q1   3.304951







###------How to move a column to the first position in a dataframe------###


Suppose 'YYYYMM' is the columns I would like to move.
I can do it using df.insert(move_to_position, col_name, col):
    df.insert(0, 'YYYYMM', df.pop('YYYYMM'))

You do not need to assign this to a variable.




###------Change column name------###
df = df.rename(columns = {'oldname':'newname', 'oldname':'newname'})




'''###------Add a new row------###'''
You can append a new row using df.loc[<index_name>, <column_name>]

    df.loc['edu1', 'reg1'] = 1

If <index_name> does not exist, pandas will create a new row.





"""


##print(df.columns)
#
#cdf = df.drop(columns = ['Unnamed: 0', 'Source', 'End_Time', 'Start_Lat', 'Start_Lng'])
#cdf = cdf.drop(columns = ['End_Lat', 'End_Lng', 'Description', 'Number', 'Street'])
#cdf = cdf.drop(columns = ['City', 'Zipcode', 'Country', 'Timezone', 'Airport_Code'])
#cdf = cdf.drop(columns = ['Weather_Timestamp', 'Pressure(in)', 'Wind_Direction'])
#cdf = cdf.drop(columns = ['Wind_Chill(F)', 'Precipitation(in)', 'Astronomical_Twilight'])
#cdf = cdf.drop(columns = ['Nautical_Twilight', 'Civil_Twilight'])
#print(cdf)
#
#cdf.to_csv('clean_df.csv', index = None)
#
#
#
#df = pd.DataFrame(['1111','12313', 'ffff'])
#df.columns = ['name']
#a = df.loc[df['name'].str.contains('fff')]
#print(a)
#
#
#

###------Math in dataframe------###

# create a df:

a =[
        [1,2,1],
        [1,2,2],
        [2,2,1],
        [2,2,1],
        ]

df = pd.DataFrame(a, columns = ['year', 'inf', 'wt'])
#          year  inf  wt
#       0     1    2   1
#       1     1    2   2
#       2     2    2   1
#       3     2    2   1

##------math of a column condition on the row values of another column------##
#Use groupby to group rows with same values. For example, if we want to sum the inflation
#rate for each year, we need to group rows according to values in 'year' col. Then sum()
#the values in 'inf' col for each group.
result = df.groupby(['year'])['inf'].sum()
print(result)
#       year
#       1    4
#       2    4

##------math between two cols condition on the row values of another column------##
# Suppose we want to multiply inf by wt then sum the product for each year, 
result = df.groupby(['year']).apply(lambda row: (row.inf * row.wt).sum())
print(result)

#       year
#       1    6          =2*1+2*2
#       2    4          =2*1+2*1

#we can further compute the weighted average, which is devide what we get above by the
#summation of weight in each year.
result = df.groupby(['year']).apply(lambda row: (row.inf * row.wt).sum()/row.wt.sum())
print(result)
#       year
#       1    2.0        =(2*1+2*2)/(1+2)
#       2    2.0        =(2*1+2*1)/(1+1)


























