
'''
    Delete Product
'''

def delete():
    import sqlite3

    productid=int(input("Enter product id"))

    con=sqlite3.connect("mydb.db")
    con.execute("delete from products where productid=?",(productid,))
    con.commit()

    print("Product deleted successfully!!!")
