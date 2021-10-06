import time

"""
如何对训练和测试数据集进行归一化？


    1. 计算训练集的均值和标准差    
    2. 将训练集的均值和标准差用于训练和测试集的归一化

这样做的好处：
1. 测试数据是模拟真实环境，测试环境有可能无法获得所有数据的均值和方差，所以要用训练集的
   比如鸢尾花iris案例中，进行预测是，每次只给一个测试样本，这个样本的均值方差是多少呢？我们无从的值。所以用训练集的mean和std
 

"""

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
import numpy as np
import pandas as pd



iris = datasets.load_iris()

data_source = pd.DataFrame(iris.data)
target_source = pd.DataFrame(iris.target)
data = data_source.iloc[:,:].values
target = target_source.iloc[:,:].values


kfold_object = KFold(n_splits = 5)

for training_index,test_index in kfold_object.split(data):
    data_training,target_training = data[training_index],target[training_index]
    data_test,target_test = data[test_index],target[test_index]
    standardscaler = StandardScaler()
    standardscaler.fit(data_training)
    """
    使用standardsclaer.mean_  查看测试集的均值，
    使用standardsclaer.scale_  查看测试集的方差，
    注意，mean_的下划线表示该参数不是用户传入的，而是经过系统计算过的参数，
    这是一种统一格式
    """
    """
    transform相当于回归中的predict，
    这里表示，将数据fit后，转化为归一后的值，
    注意，这里不会覆盖原来的data_training，而是会新建一个数据集，所以，如果你需要覆盖，可以把它赋值给原来的data_training
    """
    data_training = standardscaler.transform(data_training)
    data_test = standardscaler.transform(data_test)
    machine = KNeighborsClassifier(n_neighbors = 3)
    machine.fit(data_training,target_training)
    score = machine.score(data_test,target_test)
    print(score)
    """
    1.0
    1.0
    0.8
    0.9333333333333333
    0.8
    发现准确率大大提高了
    """

