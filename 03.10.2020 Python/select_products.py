

'''
    Select Data
'''

def select():
    import sqlite3

    con=sqlite3.connect("mydb.db")
    rows=con.execute("select * from products")

    for row in rows:
        print("Product Id: ",row[0])
        print("Product Name: ",row[1])
        print("Product Price: ",row[2])
        print()
