import pandas as pd
import numpy as np
df=pd.DataFrame({"id":[1,2,3,4],"val":[2,5,np.nan,6]})
print(df.val==np.nan)
