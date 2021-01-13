import pandas as pd
import numpy as np

df1=pd.DataFrame(np.arange(12.).reshape((4,3)),columns=list('bcd'),index=['Ohio','Texas','Colorado','abc'])
df2=pd.DataFrame(np.arange(9.).reshape((3,3)),columns=list('bad'),index=['Ohio','Texas','pqr',])

print(df1)
print(df2)


print(df1+df2)          
                 

