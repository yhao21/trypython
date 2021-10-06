import time
import numpy as np
import pandas as pd



raw_data = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(raw_data)


df = pd.DataFrame(data = raw_data, columns = ['col1', 'col2', 'col3', 'col4', 'col5'])
print('data frame')
print(df,'\n\n\n')




# retrieve columns
print(df['col1'])
# use two [] gives you the col name

print(df[['col2','col3']])


df_sub = df[['col2','col3']]


x = df_sub.iloc[:,0]
print(x,'\n\n')

ha = pd.read_csv('0908.csv')
print(ha,'\n\n')



print(ha.info())

print(ha.shape,'\n\n')

print(ha.head(1),'\n\n')

#df.drop_duplicates()


print(ha.describe(),'\n\n')

print(ha.corr())


print(ha['age']>20,"\n\n")
# the inner ha do the logic worker, it give you bool value
# the outer ha gather rows with age = true
print(ha[ha['age']>20])


print('hello')















