import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.model_selection import KFold

df = pd.read_csv('ols_dataset.csv')
#target is your y
target = df.iloc[:,2].values
#data is your explanatory variables
data = df.iloc[:,3:10].values

kfold_object = KFold(n_splits=4)
kfold_object.get_n_splits(data)

#print('\n----------------------kfold---------------\n',kfold_object)

for training_index,test_index in kfold_object.split(data):
    print('\n------------------training_index----------------\n',training_index)
    print('\n------------------test_index--------------------\n',test_index)
    ##将使用的那一部分data复制给这俩个变量
    data_training,data_test = data[training_index],data[test_index]
    target_training,target_test =target[training_index],target[test_index]
    machine = linear_model.LinearRegression()
    machine.fit(data_training,target_training)
    prediction = machine.predict(data_test)
    print('\n------------------------R2------------------\n',metrics.r2_score(target_test,prediction))




