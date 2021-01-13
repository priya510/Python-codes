'''
    Traffic light example    
'''

#Internal Package/Library
import time

def countdown(x):
    for i in range(x,0,-1):
        print(i)
        time.sleep(1)
        
    
def lightsignal():
    color="red"
    
    if(color=="red"):
        print("Color is red. Please stop!!!")
        color="green"
        countdown(10)

    if(color=="green"):
        print("Color is green. continue driving!!!")
        color="yellow"
        countdown(10)

    if(color=="yellow"):
        print("Color is yellow. Please slow down and stop!!!")
        countdown(5)

    lightsignal()


#Calling function
lightsignal()

