import pandas as pd
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

#没有header，需要手动添加，不然，第一行数据会变成header。
df = pd.read_csv('dataset_gmm.csv', header = None)
print(df)
# plt.scatter(df[0],df[1])
# plt.savefig('before_kmean.png')
# plt.show()
"""
K-mean doesn't work in this dataset(df[0],df[1]), as there're overlapping.
but human can recognize it as those cluster have different distribution.z

let's try kmean first
"""

print('silhouette score for kmean: \n')

for i in range(2,10):
    machine = KMeans(n_clusters = i)
    machine.fit(df)
    result_kmean = machine.predict(df)
    score_kmean = silhouette_score(df,result_kmean)
    print('n = ' + str(i) + '   ', score_kmean)

    # plt.scatter(df[0],df[1],c = result)
    # plt.show()
    # plt.savefig('kmean.png')

"""
let's do gmm
gmm classify point by using distribution of the points

sklearn.metrics.silhouette_score
use it to check the performance
higher = better performance
Notice, you can compare the score in the same model with different n_components, however, you cannot compare the score among different model
you cannot compare the scores of kmean and gmm when n = 3
"""

print('\nsilhouette score for gmm: \n')
for i in range(2,10):
    machine_gmm = GaussianMixture(n_components = i)
    machine_gmm.fit(df)
    result_gmm = machine_gmm.predict(df)
    score_gmm = silhouette_score(df,result_gmm)
    print('n = ' + str(i) + '   ', score_gmm)
    # plt.scatter(df[0],df[1],c = result_gmm)
    # plt.savefig('result_gmm' + str(i) + '.png')
    # plt.show()

"""
silhouette score for kmean: 

n = 2    0.4997379140477448
n = 3    0.5584175478464602
n = 4    0.5192760158404317
n = 5    0.47806495067513305
n = 6    0.44079464647867017
n = 7    0.42524190174301973
n = 8    0.4275581344661424
n = 9    0.41682620320440816

silhouette score for gmm: 

n = 2    0.43160133335273365
n = 3    0.5139641707179242
n = 4    0.43258435988343313
n = 5    0.24972620976054152
n = 6    0.26135976582985604
n = 7    0.3732932006943056
n = 8    0.3528820878980548
n = 9    0.36774907865365125


"""

"""
people use telescope take many picture of black hole, and use gmm to clustering and assembling. 
最后合成我们看到的黑洞图片

"""
