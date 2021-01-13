from sklearn.metrics import accuracy_score

y_pred=[1,1,0,1,0,0,1,0,0,0,1,1,0]
y_true=[1,0,0,1,0,0,1,1,1,0,1,0,0]
print(accuracy_score(y_true,y_pred))



'''
count=0
for x,y in zip(y_pred,y_true):

    if(x==y):
        count=count+1
        
print(count/len(y_pred))
'''


