











'''1.single inheritance:
-----------------------
A child class inherits from one parent is single inheritance
'''
class animal:
    def sound(self):
        print("Animal make sounds")
class dog(animal):
    def barks(self):
       print("Dog braks")
d = dog()
d.sound()
d.barks()

class father:
    def land(self):
        print("5 arc of land")
class son(father):
    def flat(self):
        print("3BHK")
s = son()
s.land()
s.flat()

''' multiple inheritance:
-------------------------
A child inherits more than one parent is called
'''
class father:
    def skills(self):
        print("driving")
class mother:
    def talent(self):
        print("cooking")
class son(father, mother):
    def mine(self):
        print("coding")
all = son()
all .skills()
all.talent()
all.mine()

''' multi-level
---------------
one child class becomes the parent for another class
'''
class grandfather:
    def house(self):
        print("owns house")
class father(grandfather):
    def flat(self):
        print("new flat")
class son(father):
    def car (self):
        print("have a car")
fam = son()
fam.house()
fam.flat()

''' hierarchical:
-----------------
multiple childs inherits from the same parent
'''
class mother:
    def gold(self):
        print("10 kg gold")
class pinky(mother):
    def show(self):
        print("will get 5 kg gold")
class yukatha(mother):
    def show_2(self):
        print("will get remainig 5 kg gold")
child_1 = pinky()
child_2 = yukatha()

child_1.gold()
child_1.show()

child_2.gold()
child_2.show_2()

''' hybrid:
-----------
This is the combination of two or more types of inheritance
example of multiple + multi-level
'''
class A:
    def methodA(self):
        print("class A")
class B(A):
    def methodB(self):
        print("class B")
class C(A):
    def methodC(self):
        print("class C")
class D(B, C):
    def methodD(self):
        print("class D")

so =D()
so.methodA()
so.methodB()
so.methodC()

'''super():
-----------
this super() function is used to access the parent class methods or constructor in the child class...
'''
class parent:
    def show(self):
        print("parent method")
class child(parent):
    def show(self):
        super().show()
        print("child class")
class child_2(child):
    def show(self):
        super().show()
        print("parent class")
chi = child_2()
chi.show()

class person:
    def __init__(self, name):
        self.name = name
class student(person):
    def __init__(self, name, roll):
        super().__init__(name)
        self.roll = roll
    def display(self):
         print(self.name)
         print(self.roll)
an = student("vinod", 101)
an.display()
        

