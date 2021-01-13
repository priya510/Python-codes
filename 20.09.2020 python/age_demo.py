'''
    Conditional Construct:

    WAP in python to accept age of employee and
    check whether it is valid or not.
'''

age=int(input("Enter your age"))

if(age>=18 and age<=60):
    print("Employee age is valid")
else:
    print("Employee age invalid")
