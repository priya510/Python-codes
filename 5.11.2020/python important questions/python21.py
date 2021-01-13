import pandas as pd
df=pd.DataFrame([[-1,-2,-5,-8],
                 [-9,-3,-5,-1],
                 [-1,-2,-6,-3]],
                index=pd.date_range("1/1/2000",periods=3),
                columns=["A","B","C","D"])
print(df.rolling(window=2).mean())
