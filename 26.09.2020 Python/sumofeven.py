''' WAP in python to accept five numbers in list and display sum of even numbers.
'''

NumList = []
Even_Sum = 0

Number = int(input("Please enter the  Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] % 2 == 0):
        Even_Sum = Even_Sum + NumList[j]
    
print("\nThe Sum of Even Numbers in this List =  ", Even_Sum)
