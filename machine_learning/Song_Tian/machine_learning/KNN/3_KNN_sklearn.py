from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets
import pandas as pd
import numpy as np


'''
使用sklearn中的knn方法：

首先需要导入模块：
from sklearn.neighbors import KNeighborsClassifier

然后直接使用前期处理好的数据 x_train 和 y_train，
思路和linearRegression是一样的，
先实例化一个对象machine
    machine = KNeighborsClassifier(n_neighbors = 6) 
    括号里填写你要比较最近的多少个点，这里比较的是最近的6个点
然后通过fit方法训练这个机器，
最后通过predict方法预测，

这里需要注意了！！！，sample或者是我们平时用的data_test必须是以矩阵形式呈现的，不能是[2,1]这样的一维数组，
你可以选则使用np中的reshape手动调整为(1,2)，一行两列（因为我们这里只有一个测试数据，如果多个测试数据就是n行2列）
当然也可是reshape(n,-1)填写-1是让numpy自行调整


最后返回的值是2，说明是恶性肿瘤

'''

iris = datasets.load_iris()

data_source = pd.DataFrame(iris.data)
target_source = pd.DataFrame(iris.target)
data = data_source.iloc[:,2:].values
target = target_source.iloc[:,:].values
data = np.hstack((target,data))

set1 = data[data[:,0] == 1]
set2 = data[data[:,0] == 2]

sub1 = set1[:,1:]
sub2 = set2[:,1:]
X = np.vstack((sub1,sub2))
Y = np.vstack((set1[:,0].reshape(len(set1),1),set2[:,0].reshape(len(set2),1)))

x_train = np.array(X)
y_train = np.array(Y)

machine = KNeighborsClassifier(n_neighbors = 6)
machine.fit(x_train,y_train)
sample = np.array([5.6,2]).reshape(1,-1)
prediction = machine.predict(sample)
print(prediction)
