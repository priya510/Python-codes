import pandas as pd
import numpy as np
df1=pd.DataFrame([[2.23,4.00,-6.56],
                  [8.12,-10,-12.89],
                  [14.23,-1.36,-1.8],
                  [20.56,-3.2,60.3]],columns=["col1","col2","col3"])
print(df1.reindex([0,1,2,3,4,5],method="ffill",limit=1))
