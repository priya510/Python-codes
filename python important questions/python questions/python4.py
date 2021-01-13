d={1:[0,1,2,3],2:(4,6,8,10)}
d[1].append(4)
print(d[1],end="")
l=list(d[2])
l.append(10)
d[2]=tuple(l)
print(d[2])
