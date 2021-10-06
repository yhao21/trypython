import time

"""
as kernel = 'linear' works really bad, we can create a new dimension for data and target

    x^2 + y^2 = 1 


"""

import kfold_module
from sklearn import svm
from sklearn.datasets import make_circles
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

data, target = make_circles(n_samples=500, noise=0.04)
#change it to column vector
data1 = data[:,0].reshape((-1,1))
data2 = data[:,1].reshape((-1,1))
data3 = data1**2 + data2**2

data = np.hstack((data,data3))

# print(data1,'\n\n',data2)
# print(data)

#plot a 3D picture
fig = plt.figure()
axes = fig.add_subplot(111,projection = '3d')
axes.scatter(data1,data2,data3,c = target,depthshade = True)
# plt.show()
# plt.savefig('cirle_sample_3D.png')

"""
how to draw the hyperplane to divide 3D?
we need coefficient parameter from regression

"""
machine = svm.SVC(kernel = 'linear')
machine.fit(data,target)
coeff = machine.coef_
intercept = machine.intercept_
print(coeff)
print(intercept)
"""
[[ 0.0126211  -0.05931698 -8.1820115 ]]
[6.82903446]"""
#get 0.0126211
"""3D图像的两个横坐标为x1和x2"""
data1,data2 = np.meshgrid(data1,data2)

plane = -(coeff[0][0]*data1 + coeff[0][1]*data2 + intercept)/coeff[0][2]
axes1 = fig.gca(projection = '3d')
axes1.plot_surface(data1,data2,plane,alpha = 0.01)
plt.show()








#now we use linear kernel. data has 3 dimension
##you can use polynominal kernel by kernel = 'poly'
# result_r2, result_confusion_matrix, result_accu_rate = kfold_module.run_kfold(5, data, target, svm.SVC(gamma='auto',kernel='linear'), confusion=1,use_accuracy=1)
#
#
# print(result_r2)
# print(result_accu_rate)
# for i in result_confusion_matrix:
#     print(i)

"""
you may find even we use linear kernel, the R_2 and accuracy rate are also very high. Problem solved
[0.9597423510466989, 1.0, 0.9594155844155844, 0.9599358974358975, 0.9598554797270172]
[0.99, 1.0, 0.99, 0.99, 0.99]
"""




#
#
# # result_r2, result_confusion_matrix, result_accu_rate = kfold_module.run_kfold(5, data, target, svm.SVC(gamma='auto'), confusion=1,use_accuracy=1)

#
# """
# ##what if we run kernel = 'linear', its performance is really bad
# [-1.7777777777777777, -1.3685266961059819, -0.9607843137254906, -1.2222222222222214, -1.3255813953488373]
# [0.36, 0.41, 0.51, 0.45, 0.43]
# """
# print(result_r2)
# print(result_accu_rate)
# for i in result_confusion_matrix:
#     print(i)
#
# plt.scatter(data[:, 0], data[:, 1], c=target)
# plt.show()
#
