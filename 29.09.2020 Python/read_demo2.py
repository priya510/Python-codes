
'''
    WAP to open a file, read data and store data in list.
'''

d=[]

file=open("colors.txt")
#d.extend(file.readlines())
d=file.readlines()

print(d)
for i in d:
    print(i,end="")
