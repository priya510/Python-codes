
#Calc Demo
def add(a,b):
    print("Addition: ",a+b)

def sub(a,b):
    print("Subtraction: ",a-b)

def div(a,b):
    print("Division: ",a/b)

def mul(a,b):
    print("Multiplication: ",a*b)

'''
def choice():
    ch=input("Do you want to continue with this application?")
    if(ch=="yes"):
        menu()
'''

#Recursion
def menu():
    x=int(input("Enter first number"))
    y=int(input("Enter second number"))
    
    print("========MENU==========")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Division")
    print("4. Multiplication")
    ch=int(input("Enter your choice"))

    if(ch==1):
        add(x,y)
    elif(ch==2):
        sub(x,y)
    elif(ch==3):
        div(x,y)
    elif(ch==4):
        mul(x,y)
    else:
        print("Invalid option")

    ch=input("Do you want to continue with this application?")
    if(ch=="yes"):
        menu()



menu()
