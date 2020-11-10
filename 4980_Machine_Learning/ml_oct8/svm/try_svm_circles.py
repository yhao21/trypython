import numpy as np

import kfold_template
import pandas as pd
from sklearn import svm
from sklearn.datasets import make_circles
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


data, target = make_circles(n_samples = 500, noise=0.04, random_state=0)


#print(data)
#print(target)

### identify color with the target value of these two datasets
#plt.scatter(data[:,0], data[:,1], c=target)
#plt.savefig('plot_circles.png')


#accu_score, conf_matrix = kfold_template.run_kfold\
#        (5, data, target, svm.SVC(kernel='linear', tol = 0.000001))
#
#print(accu_score)
#for i in conf_matrix:
#    print(i)
##[0.42, 0.43, 0.4, 0.47, 0.44]
## linear kernel gives bad result
#


## rbf is a non-linear kernel
#accu_score, conf_matrix = kfold_template.run_kfold\
#        (5, data, target, svm.SVC(kernel='rbf', tol = 0.000001))
#print(accu_score)
#for i in conf_matrix:
#    print(i)
#[0.99, 0.99, 0.99, 1.0, 1.0] rbf works so well


#=========================
#3D graph
#=========================

'''
There is a way we can use linear to fit data very well even if it is circle

Plot data in 3D first
'''

#trans data into 1 dimension
data1 = data[:,0].reshape((-1,1))
data2 = data[:,1].reshape((-1,1))

# distance to the origin
data3 = data1**2 + data2**2
data = np.hstack((data,data3))
# now data has three columns
#print(data)
'''
[[-0.66127655  0.76841055  1.02774145]
 [ 0.71850962  0.08784052  0.52397203]
 [ 0.56122189  0.59354738  0.6672685 ]
 ...
 [-1.09094942  0.24577934  1.25057812]
 [ 0.35620994  0.90713861  0.94978597]
 [-0.37451614 -0.98129961  1.10321126]]
'''
#fig = plt.figure()
#axes = fig.add_subplot(111,projection='3d')
#axes.scatter(data1,data2,data3,c = target, depthshade = True)
#plt.savefig('plot_3d.png')

#plt.scatter(data[:,0], data[:,1], c=target)
#plt.savefig('plot_circles.png')



'''
try to use higher dimension and linear kernel,
it will give you more accurate result than using non-linear kernel directly.
'''


## [1.0, 0.99, 0.99, 1.0, 1.0] after adding 3rd dimension, we have much higher
## score with linear kernel
machine = svm.SVC(kernel='linear', tol = 0.000001)
accu_score, conf_matrix = kfold_template.run_kfold(5, data, target, machine)
print(accu_score)
for i in conf_matrix:
    print(i)











