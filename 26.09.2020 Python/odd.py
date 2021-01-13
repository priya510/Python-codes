'''
        Accept five numbers from user and print odd numbers.
'''

t=()
print("Enter five numbers")
for i in range(5):
        t=t+(int(input()),)
        
print("odd numbers are")
for i in t:
        if(i%2!=0):
                print(i)
