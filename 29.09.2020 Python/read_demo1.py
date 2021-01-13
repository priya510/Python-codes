

#1st parameter - File Path
#2nd parameter - Mode
#                    -Read   -> "r"  (Bydefault it is read mode)
#                    -Write  -> "w"
#                    -Append -> "a"

#file=open("E:\\eclipse\\license.txt")
file=open("colors.txt","r")
print(file.read())
file.close()
