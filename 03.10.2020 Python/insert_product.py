

'''
    Insert data
'''

def insert():
    import sqlite3

    productid=int(input("Enter product id"))
    productnm=input("Enter product name")
    productpr=float(input("Enter product price"))

    con=sqlite3.connect("mydb.db")
    con.execute("insert into products values(?,?,?)",(productid,productnm,productpr))
    con.commit()

    print("Product inserted successfully!!!")
