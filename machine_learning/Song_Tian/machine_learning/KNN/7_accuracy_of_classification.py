from sklearn import datasets
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import KFold

dig = datasets.load_digits()

data = dig.data
target = dig.target
print()

df = pd.DataFrame(np.hstack((target.reshape(len(target),1),data)))

"""我们看一下data的每一行是什么样子的"""
# print(data_source[0])
# print(len(data_source[0]))
"""每一行有64个元素，我们用matplotlib的imshow方法来看一下这个数据的可视化效果是什么"""
"""8乘8的像素是非常低的，所以我们看到的是一个马赛克版的手写数字0"""
# line_0 = data_source[0].reshape(8,8)
# plt.imshow(line_0,cmap=matplotlib.cm.binary)
# plt.show()

kfold_object = KFold(n_splits = 8)


result = []
for training_index,test_index in kfold_object.split(data):
    data_training,target_training = data[training_index],target[training_index]
    data_test,target_test = data[test_index],target[test_index]

    machine = KNeighborsClassifier(n_neighbors = 15)
    machine.fit(data_training,target_training)
    prediction = machine.predict(data_test)
    #如果prediction和真实y相同返回的就是true，true = 1，然后用sum就能求出一共有多少个true
    true_prediction = sum(prediction == target_test)
    accuracy_rate = true_prediction/len(target_test)

    result.append(accuracy_rate)

print(np.array(result).reshape(len(result),1))
