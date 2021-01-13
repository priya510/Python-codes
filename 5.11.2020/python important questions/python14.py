from scipy.spatial import distance
import pandas as pd

p=pd.Series([1,2,3])
q=pd.Series([1,3,5])

print(distance.euclidean(p,q))



