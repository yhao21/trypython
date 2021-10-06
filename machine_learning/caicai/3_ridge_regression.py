from sklearn import linear_model

"""
ridge regression函数中，alpha默认值为1，可以手动修改

通过ridge regression处理cal_house数据，看看能否优化结果，若能优化，则原始数据可能存在multicollinearity
"""
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing as cal_house
from sklearn.model_selection import KFold
from matplotlib import pyplot as plt
from sklearn import metrics

x_source = pd.DataFrame(cal_house().data)
y_source = pd.DataFrame(cal_house().target)


data = x_source.iloc[:,:].values
target = y_source.iloc[:,:].values

kfold_object = KFold(n_splits = 5)


r2_result = []
for training_index, test_index in kfold_object.split(data):
    data_training,target_training = data[training_index],target[training_index]
    data_test,target_test = data[test_index],target[test_index]
    machine = linear_model.Ridge(alpha = 10)
    machine.fit(data_training,target_training)
    prediction = machine.predict(data_test)
    r2 = metrics.r2_score(target_test,prediction)
    r2_result.append(r2)

print(r2_result)

'''
[0.5574511174636827, 0.4651754698206989, 0.5505881145347796, 0.5322518702415202, 0.6615668227885956]
ridge效果并不好，初步得出结果，cal_house数据应该不是multicollinearity problem
'''