import time
"""
unsupervised learning only care about how to separate data into different groups,
it does not care about the target value of data.


K-means clustering method(KMC):
    expected maximization method
    jargon: heuristic
"""

from sklearn.datasets._samples_generator import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


data,target = make_blobs(n_samples=400, centers=4, cluster_std=0.95, random_state=420)

# print(data,'\n\n',target)

"""
as we are doing unsupervised learning, let's pretend we only have data. no target value
"""

# plt.scatter(data[:,0],data[:,1])
# plt.show()

machine = KMeans(n_clusters=4)
machine.fit(data)
results = machine.predict(data)
#ssd: sum of squared distance
ssd = machine.inertia_
centroids = machine.cluster_centers_

# print(results)
# print(machine.cluster_centers_)
print(ssd)
"""
centers:
[[-2.78930177 -8.57224992]
 [ 7.42693698  2.42606624]
 [-3.62067341 -0.97182293]
 [-4.80431977 -7.85541098]]
"""

plt.scatter(data[:,0],data[:,1], c  = results)
plt.scatter(centroids[:,0],centroids[:,1],c = 'red',marker = '*')
plt.show()


"""
在S2_KMC中，你会发现n从1到k，ssd逐渐减少，ssd的曲线和1/x相似。convex
我们使用ssd选取适当的n值。我们发现刚开始ssd下降很快，后来不怎么下降了，我们会取适中的值，比如n = 4, ssd = 642

"""


