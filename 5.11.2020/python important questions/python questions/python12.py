import numpy as np

train_set=np.array([1,2,3])
test_set=np.array([[0,1,2],[1,2,3]])

#print(train_set)
#print(test_set)

resulting_set=np.vstack([train_set,test_set])
print(resulting_set)
