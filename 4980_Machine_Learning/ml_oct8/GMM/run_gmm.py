import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture
from sklearn import metrics
from sklearn.metrics import silhouette_score


'''
silhouette_score

compare the similarity of all other dots in a group with a particular dot.
i.e.,
average distance in side a group


We cannot compare score between difference technique, i.e., kmean vs gmm
but we can compare within a technique, group 1 vs group 2 in kmean


'''



'''
Let's see if KMeans works for this gmm dataset
'''
# this dataset does not have col header, so set header = None
dataset = pd.read_csv('dataset.csv', header = None)
print(dataset)


#plt.scatter(dataset[0],dataset[1])
#plt.savefig('scatterplot.png')

for n in range(5):
    kmc_machine = KMeans(n_clusters = n+2)
    kmc_machine.fit(dataset)
    kmc_results = kmc_machine.predict(dataset)
    print('kmc')
    print('silhouette_score: group %d' % n)
    print(silhouette_score(dataset, kmc_results))
    print('\n')
#    
#    plt.scatter(dataset[0], dataset[1], c = kmc_results)
#    plt.savefig('scatterplot_kmeans_' + str(n+2) + '.png')
    

'''
You will see kmean cannot figure out the overlapping part.
We obtain a wrong classification
'''



for n in range(5):
    gmm_machine = GaussianMixture(n_components = n+2)
    gmm_machine.fit(dataset)
    gmm_results = gmm_machine.predict(dataset)
    print('gmm')
    print('silhouette_score: group %d' % (n+2))
    print(silhouette_score(dataset, gmm_results))
    print('\n')

    
    #plt.scatter(dataset[0], dataset[1], c = gmm_results)
    #plt.savefig('scatterplot_gmm_' + str(n+2) + '.png')







