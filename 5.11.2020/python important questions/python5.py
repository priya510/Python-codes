import numpy as np
from sklearn.decomposition import PCA

X=np.array([[-1,-1,2],
           [-2,-1,3],
           [-3,-2,5]])

pca=PCA(n_components=3)
pca.fit(X)
print(pca.transform(X).shape)
