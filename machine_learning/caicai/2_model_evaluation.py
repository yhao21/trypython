from sklearn import linear_model

"""
回归类模型的评估指标

回归类与分类模型的评估指标不同，分类类型的对错很明显，放对类别就是正确，否则错误
但是回归类不同，比如真实值是3.0，你预测出来的是3.01，那么我们依旧认为你的回归是比较准确的


从两个角度评判回归模型：
    1. 预测值是否准确
    2. 是否拟合到足够的信息(R2)
"""


"""使用MSE检验"""
from sklearn import linear_model
from sklearn.datasets import fetch_california_housing as cal_house
from sklearn.model_selection import KFold
from sklearn import metrics
import pandas as pd
from sklearn.metrics import mean_squared_error as MSE

x_data = pd.DataFrame(cal_house().data)
y_target = pd.DataFrame(cal_house().target)
x_data.columns = cal_house().feature_names

x_for_reg = x_data.iloc[:,:].values
y_for_reg = y_target.iloc[:,:].values

kfold_obj = KFold(n_splits = 5)


MSE_result = []
y_test_mean = []
r2_result = []
for training_ind,test_ind in kfold_obj.split(x_for_reg):
    x_for_reg_training,y_for_reg_training = x_for_reg[training_ind],y_for_reg[training_ind]
    x_for_reg_test,y_for_reg_test = x_for_reg[test_ind],y_for_reg[test_ind]
    machine = linear_model.LinearRegression()
    machine.fit(x_for_reg_training,y_for_reg_training)
    prediction_OLS = machine.predict(x_for_reg_test)
    MSE_result.append(MSE(y_for_reg_test,prediction_OLS))
    y_test_mean.append(y_for_reg_test.mean())
    r2_result.append(metrics.r2_score(y_for_reg_test,prediction_OLS))
print(MSE_result)
print(y_test_mean)
compare = [*zip(y_test_mean,MSE_result)]
print(compare)
print(r2_result)
"""
MSE
[0.48485856745731853, 0.6224973867349289, 0.6462104728578221, 0.5431995961545427, 0.4946848356387948]
y_mean
[1.6830696875, 2.2033067635658914, 2.3616295663759685, 1.8346752349806201, 2.260109593023256]

compare

[     mean                     MSE
(1.6830696875,          0.48485856745731853), 
(2.2033067635658914,    0.6224973867349289), 
(2.3616295663759685,    0.6462104728578221), 
(1.8346752349806201,    0.5431995961545427), 
(2.260109593023256,     0.4946848356387948)
]

r2_result:
[0.5486632333951383, 0.46820690860544, 0.5507843423339012, 0.5369870266519263, 0.6605140591532079]

误差太大了。。。
"""

