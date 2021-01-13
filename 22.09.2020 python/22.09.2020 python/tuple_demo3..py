'''
    WAP in python to accept five numbers and display only
    positive numbers.
'''

t=()
print("Enter five numbers")
for i in range(5):
    t=t+(int(input()),)


print("=====OUTPUT====")
for i in t:
    if(i>0):
        print(i)


