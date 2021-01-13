'''
    Self keyword:
'''

z=10                    #Global variable

class MyClass1:

    a=2                 #Member variable

    def myfunction1(self):
        a=3             #function variable, local variable
        print(a)        #3
        print(self.a)   #2
        print(z)        #10   


    def myfunction2(self):
        print(self.a)   #2
        #print(a)       #Error
        global z
        z=15            
        print(z)        #15


class MyClass2:

    def myfunction3(self):
        print(z)        #15





m1=MyClass1()
m1.myfunction1()
m1.myfunction2()


m2=MyClass2()
m2.myfunction3()

    
