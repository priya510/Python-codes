
'''
    Read image from D: drive and copy it in E: drive:
'''

#Modes
#rb - Read  binary
#wb - Write binary

file1=open("D:\\birthday.jpg","rb")
file2=open("E:\\birthday.jpg","wb")

file2.write(file1.read())
file1.close()
file2.close()

print("Image copied successfully!!!")
