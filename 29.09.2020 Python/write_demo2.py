
'''
    WAP in python to accept employee details from user
    and store in the employees.txt file.
'''

employeeid=input("Enter Employee Id: ")
employeenm=input("Enter Employee Name: ")
employeeem=input("Enter Employee Email: ")

#a+ -> Append + -> Append + Read
#r+ -> Read   + -> Read   + Append
#w+ -> Write  + -> write  + read

file=open("employees.txt","a+")
file.write(employeeid+", "+employeenm+", "+employeeem+"\n")
print("Employee data saved successfully!!!")

print("=========Employee Data=======")
file.seek(0)
print(file.read())
file.close()




