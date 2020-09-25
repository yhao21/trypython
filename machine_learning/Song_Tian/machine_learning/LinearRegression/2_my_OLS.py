import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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


data_source = pd.read_csv('ols_dataset.csv')
y = data_source.iloc[:100,2].values
x = data_source.iloc[:100,3].values



machine = LinearRegression1()
machine.fit(x,y)
prediction = machine.predict(x)
plt.scatter(x,y)
plt.plot(x,prediction)
plt.xlim([0,100])
plt.show()

from sklearn import metrics
r2 = metrics.r2_score(y,prediction)
print(r2)
"""
0.7298118292745532
R方并不高，，拟合度不高
"""