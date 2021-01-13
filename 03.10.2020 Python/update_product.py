

'''
    Update Product
'''

def update():
    import sqlite3

    productid=int(input("Enter Product Id"))
    productnm=input("Enter new product name")

    con=sqlite3.connect("mydb.db")
    con.execute("update products set productname=? where productid=?",(productnm,productid))
    con.commit()

    print("Product updated successfully!!!")
