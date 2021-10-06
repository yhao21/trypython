import time

"""
超参数hyperparameter:

在算法运行前需要决定的参数，比如knn中的k值，weights（uniform或者distance），p值（p默认为2，即欧拉距离，p = 1为曼哈顿距离）
一般机器学习工程师们所说的 “调参”，调整的就是这个超参数，，使得模型预测的准确定提高


模型参数model parameter：

算法过程中学习的参数（KNN没有模型参数，只有超参数）





如何寻找好的超参数：

    领域知识
    经验数值：比如sklearn中KNN算法中默认的k = 5，就是经验数值
    实验搜索：尝试集中不同的超参数，看准确定




"""

from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd


dig = datasets.load_digits()
data = dig.data
target = dig.target


data_training,data_test,target_training,target_test = train_test_split(data,target,test_size = 0.2)

best_score = 0.0
best_k = 1

for k in range(1,50):
    machine = KNeighborsClassifier(n_neighbors=k)
    machine.fit(data_training,target_training)
    prediction = machine.predict(data_test)
    score = sum(prediction == target_test)/len(target_test)
    if score > best_score:
        best_score = score
        best_k = k

print("best score = ",best_score,'\n\n',"best k = ",best_k)

"""
best score =  0.9916666666666667 

 best k =  4

"""




"""
注意，如果我们找到的最好的k值是48或者49，那么我们需要把k的取值在拓展一下，因为这个最有k在我们当前k取值的临界值，
所以，有可能更好的k在大于我们当前k取值的范围里








此外我们需要注意一下的情况：

令 k = 3


                                        blue1
                                        
                                                    blue2
                          green1
                            
                    red1
                    
    red3        
        red2
        
        
        
在这个案例中，我们发现，距离green1最近的三个点是“red1”，“blue1”，和“blue2”
普通KNN算法根据投票原理，会判定green1是属于blue这一类的

但是我们发现，green1距离red1非常的近，肉眼来看他很可能是属于red这一类的，
那么当这种情况发生时，我们是不是需要让red1的票的权重更大一些呢？

通常我们是把距离的倒数作为权重！！！

比如：

green1和red1的距离是1
green1和blue1的距离是3
green1和blue2的距离是4

那么考虑到距离因素，（权重等于距离的倒数）

red1的权重为1
blue1的权重为 (1/3)
blue2的权重为 (1/4)

红色的票数 = red1的权重 * red1的票数 = 1 * 1
蓝色的票数 = blue1的权重 * blue1的票数 + blue2的权重 * blue2的票数 = (1/3) * 1 + (1/4) * 1 = (7/12)

1 > (7/12)

红色票高，所以判定green1属于红色类

显然红色的权重比蓝色的高






另外一种情况是：

当我们的数据集如果种类多余2，比如我们3类，我们令k = 3时，如果恰好距离green1最近的三个点分别属于red、blue、black，
即，每个类各一个点。这种情况下，如果我们不考虑距离因素，就会出现平票的现象，即1:1:1，系统就无法判断具体属于哪一类


                                        black1
                                        
                                                    blue1
                          green1
                            
                    red1
     
   
   
但如果我们加入距离因素作为权重，我们会发现red获胜



在sklearn的KNeighborsClassifier()中，除了n_neighbors参数外，还有一个参数叫weights

weights的默认值为uniform，这时候是不考虑距离因素的，只看票数多少
如果我们使用距离作为权重，则令
weights = 'distance'

代码：
    knn_clf = KNeighborsClassifier(n_neighbors = 5,weights = 'distance')


同样，我们可以想上面的检验方法一样，来看看使用哪一种method更好
"""

data_souce = dig
x = data_souce.data
y = data_souce.target

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size = 0.3)

best_method = ''
best_accuracy = 0.0
best_k_value = 0

for method in ['uniform','distance']:
    for k in range(1,50):
        knn_clf = KNeighborsClassifier(n_neighbors = k,weights = method)
        knn_clf.fit(x_train,y_train)
        prediction_value = knn_clf.predict(x_test)
        score_value = sum(prediction_value == y_test)
        accu_rate = score_value/len(y_test)
        if accu_rate > best_accuracy:
            best_method = method
            best_accuracy = accu_rate
            best_k_value = k

print('-------------------------------')
print('best_method = ',best_method,'\n\n','best_score = ',best_accuracy,'\n\n','best_k_value = ',best_k_value)


"""
-------------------------------
 best_method =  uniform 

 best_score =  0.9888888888888889 

 best_k_value =  1


"""


"""
当然，我们也可以根据不同的距离计算公式来看knn算法的拟合准确度
具体笔记在machine_learning_notes中查看
D:\Yan\PHD PROGRAM\Class\Spring 2020\Econ 9000 Machine learning\Try_pycharm_\machine_learning


sklearn中默认的p值为2，即欧拉距离

"""