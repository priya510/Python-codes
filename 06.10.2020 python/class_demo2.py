'''
    Classes & Objects
'''

class Employee:

    empid=0
    empname=""


#objects
e1=Employee()#Constructor
e2=Employee()#Constructor

e1.empid=123
e1.empname="Rahul"

e2.empid=124
e2.empname="Prabhas"

print("=====Employee Details 1========")
print("Employee Id: ",e1.empid)
print("Employee Name: ",e1.empname)

print("=====Employee Details 2========")
print("Employee Id: ",e2.empid)
print("Employee Name: ",e2.empname)
