import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split

x=pd.DataFrame(np.srange(20).reshape((10,2)))
y=pd.Series(['A','B','C','D','E','F','G','H','I',np.nan])
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.33,random_state=123)
print("features testing data:\n",x_test)
print("prediction testing data:\n",y_test)
