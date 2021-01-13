'''
    Create database and table
'''

import sqlite3

con=sqlite3.connect("mydb.db")

#SQL - Structured Query Language
con.execute(
            '''
                create table products
                (
                    productid int,
                    productname text,
                    price float
                )
            ''')

print("Table and database created successfully!!!")
