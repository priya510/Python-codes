'''
    WAP to accept day and amount from user and check
    whether day is sunday and amount is greater than 5000
    and then print discount.

    NOTE: amount above 5000 will get 5% discount.
'''

amount=float(input("enter the amount"))
day=(input("Enter the day")).lower()

if(amount>5000 and day=="sunday"):
    print(amount * 0.05)
else:
    print("no discount")
      

