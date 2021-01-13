import pandas as pd
sdata={"Ohio":35000,"Texas":71000,"Oregon":16000,"Utah":5000}
states={"California","Ohio","Oregon","Texas"}
obj4=pd.Series(sdata,index=states)
print(pd.isnull(obj4))
