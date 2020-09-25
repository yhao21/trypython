import time


"""
support vector machine(SVM) 支持向量机

when should use SVM?
SVM doesn't support probability estimate. only classification
for classification problem, most of the time, SVM > LogisticRegression


使用make_blob创建自己的假想数据

"""
from matplotlib import pyplot as plt
from sklearn.datasets._samples_generator import make_blobs
from sklearn import svm
import kfold_module


# data, target = make_blobs(n_samples = 400, centers = 2, cluster_std=0.7)
##random_state is same as np.random.seed()
##cluster_std规定了两个cluster的离散度，数字越大越离散
data, target = make_blobs(n_samples = 400, centers = 2, cluster_std=1, random_state = 0)
target[target == 0] = -1
"""
data, target = make_blobs(n_samples = 400, centers = 4, cluster_std=0.9)
"""

# print(data)
# print(target)


plt.scatter(data[:,0],data[:,1],c = target, alpha = 0.3)
plt.savefig('sample.png')
#plt.show()




result_r2,result_confusion_matrix,result_accu_rate = kfold_module.run_kfold(5,data,target,svm.SVC(gamma='auto'),confusion = 1,use_accuracy = 1)
print(result_r2)
print(result_accu_rate)
for i in result_confusion_matrix:
    print(i)

"""([1.0, 1.0, 1.0, 1.0, 1.0], [], [])
"""
plt.show()