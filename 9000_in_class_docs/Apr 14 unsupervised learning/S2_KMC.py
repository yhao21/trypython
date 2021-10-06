from sklearn.datasets._samples_generator import make_blobs
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


data,target = make_blobs(n_samples=400, centers=4, cluster_std=0.95, random_state=420)



def run_kmeans(n):
    machine = KMeans(n_clusters=n)
    machine.fit(data)
    results = machine.predict(data)
    ssd = machine.inertia_
    centroids = machine.cluster_centers_

    # print(results)
    # print(machine.cluster_centers_)
    print(ssd)

    plt.scatter(data[:,0],data[:,1], c  = results)
    plt.scatter(centroids[:,0],centroids[:,1],c = 'red',marker = '*')
    plt.show()


run_kmeans(1)
run_kmeans(2)
run_kmeans(3)
run_kmeans(4)
run_kmeans(5)
run_kmeans(6)
run_kmeans(7)
run_kmeans(8)
run_kmeans(9)
"""
18763.34533256943
4388.760307751293
870.6269770391764
642.7425438447829
552.3988054039453
"""