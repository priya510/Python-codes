f=open("Counter_input.txt","r")
f.close()
print(f.closed)#true
f=open("Counter_input.txt","r")
print(f.closed)#false
