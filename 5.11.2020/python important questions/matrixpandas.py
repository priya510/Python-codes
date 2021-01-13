import pandas as pd
data={"a":0.536,"b":1.456,"c":2.7852}
s=pd.Series(data) 

#mat=s.as_matrix()
mat=s.values
print(mat)
