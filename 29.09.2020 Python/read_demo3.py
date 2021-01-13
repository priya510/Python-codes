
'''
    WAP in python to read file and display 3rd line
    from the file.
'''

file=open("colors.txt")
d=file.readlines()

print(d[2])
