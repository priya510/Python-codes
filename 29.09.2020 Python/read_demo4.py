
'''
    WAP in python to read file and display 3
    lines from beginning of the file.
'''

file=open("colors.txt")
d=file.readlines()

print(d[0:3])
