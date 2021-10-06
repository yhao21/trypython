import pandas as pd
import numpy as np
import kfold_module
from sklearn import linear_model
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix



"""
我们发现这个数据库中有很多的y，y is a dummpy variable

for example, y1 = male  y2 = female

logistic model is also a linear model
when you have dummy variable, use logistic model, it is better than 
"""
data_source = pd.read_csv('logistic_dataset.csv')
# here, y1 is target
target = data_source.iloc[:,1].values
data = data_source.iloc[:,3:9].values

machine = linear_model.LinearRegression()
machine.fit(data,target)
test_x = np.random.randint(0,10,(3,6))
prediction = machine.predict(test_x)
# print(prediction)
"""[5.58515802 3.63327177 2.89742717]
显然恨不准确，我们的target只有0和1"""

machine1 = linear_model.LogisticRegression()
machine1.fit(data,target)
test_x = np.random.randint(0,10,(3,6))
prediction1 = machine1.predict(test_x)
# print(prediction1)
"""
[1 1 1]
"""

r2 = kfold_module.run_kfold(4,data,target,linear_model.LogisticRegression())
# print(r2)
"""
[0.5933534356123221, 0.583945682347001, 0.586508569823394, 0.5872767696511276]
"""

result = KNeighborsClassifier()
result.fit(data,target)
prediction2 = result.predict(test_x)
# print(prediction2)


# how about predict y2
y2 = data_source.iloc[:,2].values
r2_y2 = kfold_module.run_kfold(4,data,target,linear_model.LogisticRegression())
# print(r2_y2)
"""
logistic: [0.6479269941415051, 0.5919558659464608, 0.6331858815328153, 0.6239990374375358]
"""



"""
confusion matrix

对角线上的值是你预测对的数量，其他的是你预测错的数量

"""

machine3 = linear_model.LogisticRegression()
machine3.fit(data,target)
prediction3 = machine3.predict(data)
confusion_matrix = confusion_matrix(target,prediction3)
print(confusion_matrix)
"""

        0     1
 0   [[4479  486]
 1   [ 448 4587]]
 
 
我们知道target y只有0和1 两个值，
4479表示：本应为0的时候，你预测他也是0的数量为4479，即，对于y=0这个target， 你预测对了4479个
对于y = 1 的，你预测对了4587个

448表示：本来y = 0的那些obs，你预测成了1, 这类预测错误的数量为448

这个矩阵中每一项C(ij)表示：本来属于i group的，你预测它属于j group。
所以，对角线上的值：为c(ii)表示预测正确的情况
 
 """
machine_test = linear_model.LogisticRegression()
r2_test = kfold_module.run_kfold(5,data,y2,machine_test,confusion = 1)
print(r2_test)