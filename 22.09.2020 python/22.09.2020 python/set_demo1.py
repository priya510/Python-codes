'''
    Set is unordered, heterogenous and immutable
'''

#Empty set
z=set()
print(z)

#Duplicate values are not allowed.
#Bydefault it will sort numbers in ascending order.
s={2,3,4,1,2}
print(s)

#Set doesn't support indexing.
#print(s[2])    #Error

#Heterogenous
s={1,1.2,"suresh"}
print(s)

#immutable
#s[2]=44        #Error

#Foreach loop
for i in s:
    print(i)

#If you have any value other than numberic
#It takes random data
s={"a","b","d","c"}
print(s)










