#from sklearn.datasets._samples_generator import make_blobs
'''
new version of sklearn writes make_blobs directly under datasets module
'''
from sklearn.datasets import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

'''
in real world, we only have data. we don't have target
We manually generate target in this case. and we know there are 4 gourps

With real data, we need to estimate target with data.
'''

data,target = make_blobs(n_samples=400, centers=4, cluster_std=0.95, random_state=0)
#print(data)


#plt.scatter(data[:,0], data[:, 1])
#plt.savefig('scatterplot.png')
#plt.clf()


## with real data, we don't know the n_cluster, we need to find it
#machine = KMeans(n_clusters = 4)
#machine.fit(data)
#results = machine.predict(data)
## compute the center of the groups
#centroids = machine.cluster_centers_
####648.2456950378336
####ssd: sum of squared distance is the inertia_
#print(machine.inertia_)
#
#
## we color the data with the results we get
#plt.scatter(data[:,0], data[:, 1], c = results)
### s = 200 make the marker bigger
#plt.scatter(centroids[:, 0], centroids[:,1], c = 'red', marker = '*', s = 200)
#plt.savefig('scatterplot_color.png')



'''
How to measure the result?
'''


def run_kmeans(n):

    # with real data, we don't know the n_cluster, we need to find it
    machine = KMeans(n_clusters = n)
    machine.fit(data)
    results = machine.predict(data)
    # compute the center of the groups
    centroids = machine.cluster_centers_
    ###648.2456950378336
    ###ssd: sum of squared distance is the inertia_

    print('number of centers: ', n)
    print(machine.inertia_)
    

    # we color the data with the results we get
    plt.scatter(data[:,0], data[:, 1], c = results)
    ## s = 200 make the marker bigger
    plt.scatter(centroids[:, 0], centroids[:,1], c = 'red', marker = '*', s = 200)
    plt.savefig('scatterplot_color' + str(n) + '.png')
    ## must clear the graph after each round, otherwise, you will have many
    ## centers leftover.
    plt.clf()



for i in range(2,6):
    run_kmeans(i)

'''
number of centers:  2
1951.791367941146
number of centers:  3
1115.5301111206056
number of centers:  4
648.2456950378336
number of centers:  5
567.2618076986575


inertia goes down when number of center increase. This is reasonable.
inertia is the distance, and it must be going down when number of centers rises
'''







