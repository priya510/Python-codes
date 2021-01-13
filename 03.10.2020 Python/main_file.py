#Modularization
import insert_product
from select_products import select
import delete_product
import update_product

def menu():
    print("========MENU========")
    print("1. Insert Product")
    print("2. Delete Product")
    print("3. Update Product")
    print("4. Select Products")
    ch=int(input("Select one option"))

    if(ch==1):
        insert_product.insert()
    elif(ch==2):
        delete_product.delete()
    elif(ch==3):
        update_product.update()
    elif(ch==4):
        select()
    else:
        print("Invalid option")

    
    c=input("Do you want to continue with this app?")
    if(c=="yes"):
        menu()


menu()
        
