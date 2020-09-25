from sklearn.model_selection import train_test_split
import pandas as pd



df = pd.read_csv('ols_dataset.csv')
data = df.iloc[:,3:10].values
target = df.iloc[:,2].values

data_training,data_test,target_training,target_test = train_test_split(data,target,test_size = 0.25,random_state = 0)


print('\n\n\n-------------------data_training-----------------------\n\n\n',data_training)
print('\n\n\n-------------------data_test---------------------------\n\n\n',data_test)
print('\n\n\n-------------------target_training---------------------\n\n\n',target_training)
print('\n\n\n-------------------target_test-------------------------\n\n\n',target_test)




print(type(df.iloc[:,3:10]))
print(type(df.iloc[:,3:10].values))


"""
<class 'pandas.core.frame.DataFrame'>
<class 'numpy.ndarray'>
注意了，不加.values输出的是dataframe格式，加上.values输出的才是数组类型

"""