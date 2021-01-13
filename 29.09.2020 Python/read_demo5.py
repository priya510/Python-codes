
'''
    WAP in python to read file and display 3
    lines from end of the file.
'''

file=open("colors.txt")
d=file.readlines()

print(d[-1:-4:-1])
