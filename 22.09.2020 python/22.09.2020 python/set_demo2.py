'''
    WAP in python to accept five names from user
    display one lucky winner.
'''

s=set()
print("Enter five names")
for i in range(5):
    s.add(input())

print("=========OUTPUT=========")
count=1
for i in s:
    if(count>2):
        break
    
    print(i,"is a lucky winner")
    count=count+1
    


