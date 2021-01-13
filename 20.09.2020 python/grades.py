'''
    WAP in python to accept percentage from user and print grade.

        per>=75 -> Grade A
        per>=65 -> Grade B
        per>=55 -> Grade C
        per>=45 -> Grade D
        per>=35 -> Grade E
        per< 35 -> Grade F
'''

pr=int(input("enter the percentage"))

if(pr>=75):
    print("grade a")
elif(pr>=65):
    print("grade b")
elif(pr>=55):
    print("grade c")
elif(pr>=45):
    print("grade d")
elif(pr>=35):
    print("grade e")
else:
    print("grade f")
        
