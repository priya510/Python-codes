import pandas as pd
d={"Name":pd.Series(["Tom","James","Ricky","Steve","Steve","Smith","Back","Bee","Bavid","","Basper","Andres"]),
   "Age":pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   "Rating":pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

df=pd.DataFrame(d)
#Bydefault describe function will give number values.
print(df.describe(include='all'))
