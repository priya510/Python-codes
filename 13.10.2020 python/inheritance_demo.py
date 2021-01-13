'''
    Inheritance
'''

class Animal:               #Parent, Super, Base class
    def foodHabits(self):
        pass

    def nooflegs(self):
        print("4 legs")
        
        
class Herbivorous(Animal):  #Child, Sub, Derived class
    def foodHabits(self):
        print("Herbivorous eats only plants")


class Carnivorous(Animal):  #Child, Sub, Derived class
    def foodHabits(self):
        print("Carnivorous eats only meat")


h=Herbivorous()
c=Carnivorous()

h.foodHabits()
h.nooflegs()

c.foodHabits()
c.nooflegs()
