import time

"""
R square


formula is in machine learning notes



"""

import numpy as np
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import matplotlib.pyplot as plt


data_source = datasets.load_boston()

#这里我们使用RM这个数（即房间数量多少）
# print(data_source.feature_names)
RM = data_source.feature_names[5]
# print(RM)
#取出RM数据
x = np.array(data_source.data[:,5])
y = np.array(data_source.target)
#我们发现y = 50时，发现一些水平分布的值，这可能是因为我们在收集数据时设置了最大值，比如，房子价值这个问题是有一个选项是超过50
#那么我们在回归时候，要删除这些outlier
# plt.scatter(x,y)
# plt.show()
x = np.array(x[y<50.0]).reshape(len(x[y<50.0]),1)
y = np.array(y[y<50.0]).reshape(len(y[y<50.0]),1)

machine = LinearRegression()
machine.fit(x,y)
prediction = machine.predict(x)


R2 = 1 - (np.sum((prediction - y)**2)/np.sum((np.mean(y) - y)**2))
print(R2)
"""0.4714666814451758"""
print(metrics.r2_score(y,prediction))
"""0.4714666814451758"""

"""
验证成功，手写的与sklearn封装的是相同结果
"""