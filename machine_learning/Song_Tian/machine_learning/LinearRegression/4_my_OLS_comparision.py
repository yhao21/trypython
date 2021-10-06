import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
"""
非向量法实现OLS（运行速度慢）
"""

class LinearRegression1:

    def __init__(self):
        self.a_ = None
        self.b_ = None

    def fit(self,x_train,y_train):

        assert x_train.ndim ==1, \
            'this machine can only solve 1 dimension problem'
        assert len(x_train) == len(y_train), \
            'x_train and y_train must have same rows'

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)
        numerator_a = np.sum((x_train - x_mean) * (y_train - y_mean))
        denominator_a = np.sum((x_train - x_mean) ** 2)
        self.a_ = numerator_a / denominator_a
        # b = y_bar - a * x_bar
        self.b_ = y_mean - self.a_ * x_mean


    def predict(self,x_test):

        assert x_test.ndim == 1, \
            'this machine can only solve 1 dimension problem'
        assert self.a_ is not None and self.b_ is not None, \
            'you have to fit the machine before you predict!'
        y_hat = self.a_ * x_test + self.b_

        return y_hat



"""
向量法实现OLS（提升运算速度）
"""

class LinearRegression2:

    def __init__(self):
        self.a_ = None
        self.b_ = None

    def fit(self,x_train,y_train):

        assert x_train.ndim ==1, \
            'this machine can only solve 1 dimension problem'
        assert len(x_train) == len(y_train), \
            'x_train and y_train must have same rows'

        x_mean = np.mean(x_train)
        y_mean = np.mean(y_train)
        numerator_a = (x_train - x_mean).dot(y_train - y_mean)
        denominator_a = (x_train - x_mean).dot((x_train - x_mean))
        self.a_ = numerator_a / denominator_a
        # b = y_bar - a * x_bar
        self.b_ = y_mean - self.a_ * x_mean


    def predict(self,x_test):

        assert x_test.ndim == 1, \
            'this machine can only solve 1 dimension problem'
        assert self.a_ is not None and self.b_ is not None, \
            'you have to fit the machine before you predict!'
        y_hat = self.a_ * x_test + self.b_

        return y_hat



sample_size = 1000000
sample_x = np.random.randint(0,500,size = sample_size)
#np.random.normal(size=sample_size)是随机干扰项，为了破坏完整的线性关系的，
sample_y = 1.5 * sample_x + 7 + np.random.normal(0,1000,size=sample_size)
machine1 = LinearRegression2()
s_t = time.time()
machine1.fit(sample_x,sample_y)
prediction = machine1.predict(sample_x)
e_t = time.time()
print('total time: ',e_t - s_t)
# plt.scatter(sample_x,sample_y)
# plt.plot(sample_x,prediction,color = 'yellow')
# plt.show()
"""
machine1 total time: 0.023929595947265625
machine2 total time: 0.019947290420532227

第一种方法部分用了numpy的乘法，
第二种方法使用了numpy的矩阵乘法
方法二比方法一快，
这两种方法都比使用for循环快很多倍，向量运算比for循环快50倍
"""