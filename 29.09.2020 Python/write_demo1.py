

#If you are trying to write something in the file.
#And if that file doesn't exist.
#Then python will create a file for you.

file=open("foo.txt","a")
file.write("Hello World\n")
file.close()
print("Write operation is successfull")
