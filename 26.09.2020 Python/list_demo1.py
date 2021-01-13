'''
    List is ordered, mutable, heterogenous
'''

#Emtpty List
L=[]
print(L)

L=[11,22,13,41,56]
print(L)

#Indexing
print(L[0])
print(L[1])
print(L[2])
print(L[3])
print(L[4])

#Mutable
L[2]=34
print(L)

#Heterogenous
L=[1,1.2,"Sameer"]
print(L)

#Foreach Loop
for i in L:
    print(i)


#Append Vs Extend

L1=[5,9,8]
L2=[7,5,6]

L1.append(L2)
print(L1)


L1=[5,9,8]
L2=[7,5,6]

L1.extend(L2)
print(L1)


#Put single value in list
L=[1,2,3]
L.append(5)
print(L)

#Extend only takes list and will not take single value.
#L=[1,2,3]
#L.extend(5)
#print(L)


#Slicing
L=[2,1,4,5,3]       #[3,5,4,1,2]

print(L[3])
print(L[1:4])
print(L[2:5])
print(L[0:3])

print(L[-1])
print(L[-1:-4:-1])
print(L[-1:-6:-2])
print(L[-1:-6:-1])
print(L[-1::-1])
print(L[::-1])



#Built-in functions.
L.reverse()
print(L)

#Sort in ascending order
L.sort()
print(L)

#Sort in descending order
L.sort(reverse=True)
print(L)


#Slicing in nested list
L=[1,2,3,[8,9,6]]
print(L[3][1])


#List is mutable
#Delete an element

L=[1,3,4,5]

del L[1]            #Delete by index position
print(L)

L.remove(5)         #Delete by value
print(L)
















