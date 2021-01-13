import pandas as pd
from datetime import datetime
from datetime import date

'''
#System Date
print(date.today())

#System Date Time
print(datetime.today())

#System Time
print(datetime.now().time())
'''


start=datetime(2011,5,1)
index=pd.date_range(start,periods=10,freq="D")
print(index)



