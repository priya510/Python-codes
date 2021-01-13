import pandas as pd

df=pd.DataFrame({"A":[2,4,8,0],
                "B":[2,0,0,0],
                "C":[10,2,1,8],
                 "D":[4,6,1,0]},
                index=["W","X","Y","Z"])

df["A"].sample(n=3,random_state=1)
print(df)


