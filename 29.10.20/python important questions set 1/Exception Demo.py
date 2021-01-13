

try:
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))

    c=a/b

except ValueError as ve:
    print("Please enter correct value")
    
except Exception as e:
    print(e)
    
else:
    print("Division: ",c)
    
