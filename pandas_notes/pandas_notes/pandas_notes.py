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



25. extract a particular value from df

    value = df.loc[[row_index]][column_name].values[0]




"""


#print(df.columns)

cdf = df.drop(columns = ['Unnamed: 0', 'Source', 'End_Time', 'Start_Lat', 'Start_Lng'])
cdf = cdf.drop(columns = ['End_Lat', 'End_Lng', 'Description', 'Number', 'Street'])
cdf = cdf.drop(columns = ['City', 'Zipcode', 'Country', 'Timezone', 'Airport_Code'])
cdf = cdf.drop(columns = ['Weather_Timestamp', 'Pressure(in)', 'Wind_Direction'])
cdf = cdf.drop(columns = ['Wind_Chill(F)', 'Precipitation(in)', 'Astronomical_Twilight'])
cdf = cdf.drop(columns = ['Nautical_Twilight', 'Civil_Twilight'])
print(cdf)

cdf.to_csv('clean_df.csv', index = None)



df = pd.DataFrame(['1111','12313', 'ffff'])
df.columns = ['name']
a = df.loc[df['name'].str.contains('fff')]
print(a)





