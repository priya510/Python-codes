import pandas as pd
import numpy as np

df=pd.DataFrame({"A":[1,5,3,4,2],
                 "B":[3,2,4,3,4],
                 "C":[2,2,7,3,4],
                 "D":[4,3,6,12,7]},
                columns=["A","B","C","D"])

#Row    - 0
#Column - 1
print(df.apply(np.mean,axis=1))
