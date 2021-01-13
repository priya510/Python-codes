import pandas as pd
df=pd.DataFrame([[0.23,1.56,-0.45],
                 [1.2,-2.1,1.5],
                 [-5.1,3.2,-6.5],
                 [0.25,-0.36,-89],
                 [0.39,-0.78,-1.58]],index=["a","c","e","f","h"],columns=["one","two","three"])

df=df.reindex(["a","b","c","d","e","f","g","h"])
print(df["one"].sum())
