import time


"""
回顾建模过程：

step1
使用训练集训练machine，然后得到一个模型

step2
给模型传入新的测试数据，求出预测值



这样会有两个问题：
1. 我们得到的模型是一个固定的模型，没有进一步学习的能力，如果我们训练出来的模型很差，那么到实际运用中我们将面临很大的预测误差
2. 真实世界中，测试集是很难找到对应的target（y值）得，所以很难进一步改进模型

这个问题的一个原因是：我们用全部的训练数据去训练。
那么我们可以通过把训练集切分为测试和训练集，train_test_split



"""

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import pandas as pd
import numpy as np

x = datasets.load_iris().data
y = datasets.load_iris().target

print(y.shape)
"""
我们发现，y是150个元素的一维数组，里面的数据都是排好序的，前50个为0，中间50为1，后面50为2
如果我们直接切分为训练和测试集，比如我们让前100个当做训练，后50为测试，那么，训练集中将没有y=2的观测值，，
自然我们的模型就是残缺的
所以我们要先shuffle一下，把顺序打乱
两种方法：
1. 我们要先把x和y合并，，然后再shuffle，不然x和y无法对应

2. 我也可以只对x和y中的索引（数据编号）进行乱序处理，这样我们后面只需要将序号一一对应就可以了，运算量还小


"""
shuffle_indexes = np.random.permutation(len(x))
#规定测试数据及的比例，比如这里规定20%的数据用来测试
test_ratio = 0.2
#测试数据及的大小 =  x中行数乘以比例，乘法后是一个浮点数，我们要把他转成整数
test_size = int(len(x) * test_ratio)
#那么测试数据集中有哪些元素呢，我们就在shuffle_indexes中取出前test_size个，你也可以取后面的
test_indexes = shuffle_indexes[:test_size]
#训练集就是第30到最后一个数据
train_indexes = shuffle_indexes[test_size:]

#然后我们就可以取出数据各自的数据集了
x_train = x[train_indexes]
y_train = y[train_indexes]

x_test = x[test_indexes]
y_test = y[test_indexes]


machine = KNeighborsClassifier(n_neighbors = 6)
machine.fit(x_train,y_train)
prediction = machine.predict(x_test)
##查看预测出来的分类与真实分类的接近程度：计算有多少个预测出来的分类与实际分类相同，然后除以测试集的数据总量，就得到了一个百分比
score = (sum(prediction == y_test))/len(y_test)
print(score)




