import numpy as np
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
X=np.array([[-1,-1],
            [-2,-5],
            [200,800],
            [3,1],
            [2,3],
            [50,10],
            [-1,-3]])

Y=np.array([0,0,2,1,1,2,0])
clf=LinearDiscriminantAnalysis()
clf.fit(X,Y)
print(clf.predict([[-1,-3]]))
