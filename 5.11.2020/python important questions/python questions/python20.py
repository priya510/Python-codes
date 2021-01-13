import pandas as pd
data1={"men":[50,20,60,30,50,60],"Women":[40,50,60,30,10,60]}
df=pd.DataFrame(data1,index=pd.period_range("1-2004","6-2004",freq="M"))
Roll_mean=df.rolling(3,min_periods=1).mean()
print(Roll_mean)
