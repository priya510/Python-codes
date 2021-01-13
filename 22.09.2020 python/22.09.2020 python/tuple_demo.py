'''
    Tuple is ordered, heterogenous, immutable
'''

z=(11,21,13)
print(z)

#It supports indexing. Means it is ordered.
print(z[0])
print(z[1])
print(z[2])

print()
for i in range(0,3):
    print(z[i],end=" ")

print()
for i in range(2,-1,-1):
    print(z[i],end=" ")
    
print()
for i in z:
    print(i,end=" ")



z=(11,21,13,85,69)

print()
for i in range(4,-1,-1):
    print(z[i],end=" ")

print()
t=("suresh","ramesh","hitesh","paresh")
print(t)

#Heterogenours
t=(1,1.2,"mahesh",True)
print(t)

#It is Immutable. Means you cannot modify value.
#z[0]=31      #Error
#print(z)


t1=("Suresh",)
t2=("Hitesh","Jayesh")

print(t1+t2)





















