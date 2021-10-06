import time

"""
Radial basis function kernel


"""
import kfold_module
from sklearn import svm
from sklearn.datasets import make_circles
import matplotlib.pyplot as plt


#change noise to 0.1, accuracy rate decrease, point can be overlapping
data, target = make_circles(n_samples=500, noise = 0.1)


##kernel = 'linear'  R_2 is low, change kernel to 'rbf'  for radial basis function
##you can change gamma in SVC function to adjust your machine.
result_r2,result_confusion_matrix,result_accu_rate = kfold_module.run_kfold(5,data,target,svm.SVC(gamma='auto'),confusion = 1,use_accuracy = 1)
print(result_r2)
print(result_accu_rate)
for i in result_confusion_matrix:
    print(i)

plt.scatter(data[:,0],data[:,1],c = target)
plt.show()