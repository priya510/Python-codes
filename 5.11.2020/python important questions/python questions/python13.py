import pandas as pd
df=pd.DataFrame({"click_id":['A','B','C','D','E'],'Count':[100,200,300,400,250]})
print(df)


df.rename(columns={"Count":"Click_Count"})
print(df.columns)
