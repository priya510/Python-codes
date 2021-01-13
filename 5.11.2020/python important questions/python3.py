import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
X=np.array([[5,3],
            [10,15],
            [15,12],
            [60,78],
            [55,52],
            [80,91],])

kmeans=KMeans(n_clusters=2)
kmeans.fit(X)
plt.scatter(X[:,0],X[:,1],c=kmeans.labels_,cmap='rainbow')
plt.show()
