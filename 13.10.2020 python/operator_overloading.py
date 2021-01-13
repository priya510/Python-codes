'''
    Operator Overloading
'''

class Circle:
    
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return 3.14*self.radius**2
    
    def __add__(self,another_circle):
        return Circle(self.radius+another_circle.radius)

    def __sub__(self,another_circle):
        return Circle(self.radius-another_circle.radius)

    def __mul__(self,another_circle):
        return Circle(self.radius*another_circle.radius)

    def __truediv__(self,another_circle):
        return Circle(self.radius/another_circle.radius)

    def __floordiv__(self,another_circle):
        return Circle(self.radius//another_circle.radius)

    def __mod__(self,another_circle):
        return Circle(self.radius%another_circle.radius)

    def __gt__(self,another_circle):
        return self.radius>another_circle.radius

    def __gt__(self,another_circle):
        return self.radius>another_circle.radius

    def __lt__(self,another_circle):
        return self.radius<another_circle.radius

    def __ge__(self,another_circle):
        return self.radius>=another_circle.radius

    def __le__(self,another_circle):
        return self.radius<=another_circle.radius

    def __eq__(self,another_circle):
        return self.radius==another_circle.radius

    def __ne__(self,another_circle):
        return self.radius!=another_circle.radius
    
    def __str__(self):
        return "Radius: "+str(self.radius)

    
c1=Circle(5)
c2=Circle(6)

c3=c1+c2
c4=c3+c2
print(c1)
print(c2)
print(c3)
print(c4)

print(c1-c2)
print(c1/c2)
print(c1//c2)
print(c1*c2)
print(c1>c2)
print(c1<c2)
print(c1>=c2)
print(c1<=c2)
print(c1==c2)
print(c1!=c2)
print(c1.area())



