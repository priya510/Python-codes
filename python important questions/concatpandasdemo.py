import pandas as pd
left=pd.DataFrame({
     "id":[1,2,3,4,5],
     "a":["Ent1","Ent2","Ent3","Ent4","Ent5"],
     "b":["sub1","sub2","sub4","sub6","sub5"]})

right=pd.DataFrame({
     "id":[1,2,3,4,5],
     "a":["Enta","Entb","Entc","Entd","Ente"],
     "b":["sub2","sub4","sub3","sub6","sub5"]})



frames=[left,right]
print(pd.concat(frames))
