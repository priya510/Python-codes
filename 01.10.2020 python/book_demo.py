'''
    WAP to accept book details from user:

	Book
		-bookname	(Harry Potter)
		-author		(J.K Rowling)
		-price		(280)


	Folder	
		Harry Potter.txt
			Book Name: Harry Potter
			Author   : J.K Rowling
			Price    : 280


		2 States.txt
			Book Name: 2 States
			Author   : Chetan Bhagat
			Price    : 180
'''

bname=input("Enter book name: ")
bauthor=input("Enter Author: ")
bprice=input("Enter price: ")

file=open(bname+".txt","w")
file.write("Book Name: "+bname+"\n")
file.write("Book Author: "+bauthor+"\n")
file.write("Book Price: "+bprice+"\n")

print("book details saved successfully!!!")

file.close()



