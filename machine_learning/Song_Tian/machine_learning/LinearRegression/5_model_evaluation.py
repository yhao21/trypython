import time

"""

Model evaluation


MSE

RMSE

MAE

"""

import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt


data_source = datasets.load_boston()
# print(data_source.DESCR)

#这里我们使用RM这个数（即房间数量多少）
print(data_source.feature_names)
RM = data_source.feature_names[5]
print(RM)
#取出RM数据
x = np.array(data_source.data[:,5])
y = np.array(data_source.target)
#我们发现y = 50时，发现一些水平分布的值，这可能是因为我们在收集数据时设置了最大值，比如，房子价值这个问题是有一个选项是超过50
#那么我们在回归时候，要删除这些outlier
# plt.scatter(x,y)
# plt.show()
x = np.array(x[y<50.0]).reshape(len(x[y<50.0]),1)
y = np.array(y[y<50.0]).reshape(len(y[y<50.0]),1)
# plt.scatter(x,y)
# plt.show()
machine = LinearRegression()
machine.fit(x,y)
prediction = machine.predict(x)
plt.plot(x,prediction,color = 'yellow')
# plt.scatter(x,y)
# plt.show()

"""
MSE:    32.629908144716346
"""
MSE = np.sum((prediction - y)**2)/len(y)
print(MSE)

"""
RMSE:   5.712259460556422
"""
RMSE = np.sqrt(MSE)
print(RMSE)

"""
MAE:    4.1108370989454235
"""
MAE = np.sum(np.absolute(prediction - y))/len(y)
print(MAE)

"""
RMSE 比 MAE的结果略大一些原因如下：

RMSE是先对误差取平方再开方，如果一个观测值和预测值的误差是100，平方后就是10000，即便其他观测值的误差很小，最后加总后的MSE还是会很大
所以，MSE和RMSE的大小会受到误差大的预测值的影响。但MAE不会
所以，我们一般更倾向于使用MSE或者RMSE，因为如果这两个检测值的数很小的话，说明这个model的最大误差也很小。
这就说明这个model是比较好的

"""