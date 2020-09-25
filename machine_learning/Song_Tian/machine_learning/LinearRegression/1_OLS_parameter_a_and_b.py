import time

"""
几乎所有参数学习算法都是这样的套路：

线性回归        SVM
多项式回归      神经网络         总目标：最优化原理（包括凸优化）
逻辑回归



在machine_learning_notes的least squared basic中推导出了a和b的表达式
那么就可以推导出y(hat) = ax + b

我们通过代码来实现一下：
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression


data_source = pd.read_csv('ols_dataset.csv')
y = data_source.iloc[:100,2].values
x = data_source.iloc[:100,3].values


# mean of x
x_bar = np.mean(x)
# mearn of y
y_bar = np.mean(y)

numerator_a = np.sum((x-x_bar)*(y-y_bar))
denominator_a = np.sum((x-x_bar)**2)
a = numerator_a/denominator_a
# b = ax(bar) + y(bar)
b = y_bar - a*x_bar

y_hat = a*x + b
plt.plot(x,y_hat)
plt.scatter(x,y,alpha=0.3)
plt.show()

