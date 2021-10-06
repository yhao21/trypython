import numpy as np
from collections import Counter
from sklearn import datasets
import pandas as pd
"""
这里我们模拟一下sklearn是如何封装算法的


规定：
classification = 1  表示COVID test negative
classification = 2  表示COVID test positive

"""



class KNNClassifier:

    def __init__(self,k):
        assert k >= 1, 'k must be a positive number greater than 1'
        self.k = k
        self._x_train = None
        self._y_train = None

    def fit(self,x_train,y_train):
        '''断言中规范了传入的训练集必须包含相同数量的数据，即observations'''

        assert x_train.shape[0] == y_train.shape[0], \
            'size of x_train and y_train must be equal'
        assert self.k <= x_train.shape[0], \
            'k must be less than the number of observations in your training sets'
        self._x_train = x_train
        self._y_train = y_train
        return self
        #这里返回self是因为sklearn中的统一格式，这样以后如果自己写了算法可以无缝放到sk包中

    def predict(self,x_test):
        '''断言中规范了x测试集必须是n行2列的矩阵'''

        assert x_test.shape[1] == 2, \
            'x_test must be a n by 2 matrix. Use ".reshape(len(x_test),2)" to reshape your matrix'
        assert self._x_train is not None and self._y_train is not None, \
            'you should fit the machine before prediction!'
        self._x_test = x_test

        result = []
        result_index = []
        p_n = []
        #对测试集中的每一行数据（即，每一个ob）执行KNN算法
        for round in range(len(self._x_test)):

            distance = []
            #计算第round个测试集中的数据与其他所有训练集x中的元素的距离，并取出与该测试数据最近的k个训练元素，
            #判断这些训练元素的y值为1的多还是为2的多
            #最后以最多的哪一类定性测试ob属于y = 1还是y = 2
            for i in range(self._x_train.shape[0]):
                d = np.sqrt((self._x_test[round][0] - self._x_train[i,0])**2 + (self._x_test[round][1] - self._x_train[i,1])**2)
                distance.append(d)

            order = np.argsort(distance)
            nearest_k = [list(self._y_train[i]) for i in order[:self.k]]
            nearest_k = [j for i in nearest_k for j in i]
            counter = Counter(nearest_k).most_common(1)[0][0]
            result.append(counter)
            result_index.append(round)
            if counter == 1.0:
                p_n.append('negative')
            elif counter == 2.0:
                p_n.append('positive')
        #将测试集数据的序号，数据，和经过判断的classification封装到DataFrame中返回
        result = np.array(result).reshape(len(result),1)
        result_index = np.array(result_index).reshape(len(result_index),1)
        p_n = np.array(p_n).reshape(len(p_n),1)
        KNN_Classification = pd.DataFrame(np.hstack((result_index,x_test,result,p_n)))
        KNN_Classification.columns = ['obs #','x1','x2','classification','COVID test']

        return KNN_Classification


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

# 模拟一个测试集,传入的数据集必须是 n by 2 的矩阵。k不能大于50，因为内置训练集为50。可在main()中手动更换训练集
# np.random.seed(99)
x_test = np.random.normal(4,4,(10,2))

machine = KNNClassifier(k = 6)
machine.fit(x_train,y_train)
prediction = machine.predict(x_test)
print(prediction)

#prediction.to_csv('COVID_test.csv')


