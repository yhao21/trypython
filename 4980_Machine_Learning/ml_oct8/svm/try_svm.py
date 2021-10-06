
import kfold_template
import pandas as pd
from sklearn import svm
from sklearn.datasets._samples_generator import make_blobs
from matplotlib import pyplot as plt


#data, target = make_blobs(n_samples = 400, centers = 2, cluster_std=1, random_state = 1)
#data, target = make_blobs(n_samples = 400, centers = 2, cluster_std=1, random_state = 3)
data, target = make_blobs(n_samples = 400, centers = 2, cluster_std=1, random_state = 0)


#print(data)
#print(target)

## identify color with the target value of these two datasets
#plt.scatter(data[:,0], data[:,1], c=target)
#plt.savefig('plot.png')

#accu_score, conf_matrix = kfold_template.run_kfold\
#        (5, data, target, svm.SVC(kernel='linear'))

#accu_score, conf_matrix = kfold_template.run_kfold\
#        (5, data, target, svm.SVC(kernel='linear', tol = 0.000001))
# tol is tolarance level. it can be used for complicated case where dots
# are close to each others.

# use polynomial method gives you diff accu_score
accu_score, conf_matrix = kfold_template.run_kfold\
        (5, data, target, svm.SVC(kernel='poly', degree=10, tol = 0.000001))


print(accu_score)
for i in conf_matrix:
    print(i)

'''
[0.9875, 0.9625, 0.9875, 0.9625, 0.9875]
[[40  0]
 [ 1 39]]
[[37  1]
 [ 2 40]]
[[38  1]
 [ 0 41]]
[[42  2]
 [ 1 35]]
[[38  1]
 [ 0 41]]
'''






