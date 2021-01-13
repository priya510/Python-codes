import pandas as pd
import numpy as np

X=pd.DataFrame(np.arange(29.5).reshape((6,5)))
rows=X.sample(n=3)
print("Sampled rows: \n",rows)
