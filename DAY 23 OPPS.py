''' polymorphism:
---> polymorphism means many form
----> it allows same method, function or operator to perform different tasks depending on the same object...

types:
-----
method overloading:
------------------
----> method overloading means having multiple methods with the same name but different parameters

2.method overriding
3.operator overloading
'''
class cal:
    def add(self, num, num_2=0):
        print(num + num_2)
        
    def add(self, a, b):
        print(a+b)
obj = cal()
obj.add(45, 67)
obj.add(6, 5)

'''2.method overriding
----------------------
---> the method overriding occurs when a child class provides its own implementation  of a method already defined in its parent class...
'''

class animal:
    def sound(self):
        print("animals make sounds")
class dog(animal):
    def sound(self):
        print("dogs barks")
d = dog()
d.sound()

'''3.operator overloading
-------------------------
--> this allows operators (+, -, *) to work differently for user-defined objects

1.__add__(+)
2.__sub__(-)
3.__mul__(*)
4.__truediv__(/)
5.__ep__()==
6.__it__() <
'''
class student:
    def __init__(self, marks):
        self.marks = marks
    def __add__(self, other):
         return self.marks -  other.marks
s1 = student(67)
s2 = student(56)
print(s1 + s2)

'''Data abstraction:
--------------------
---> Data abstraction is the process of hiding implementation details and showing only the essentail data to the user
eg:
---
--ATM
--CAR
---APP

from abc import ABC, abstractmethod
class parent:

    @abstractmethod
    def display(self):
        pass
'''
from abc import ABC, abstractmethod

class bank:
    @abstractmethod
    def interest(self):
        raise NotImplementedError('Subclass must implement interset()')
    
class SBI(bank):
    def interest(self):
        print('SBI interest Rate: 6.5%')
        
class HDFC(bank):
    def interest(self):
        print('HDFC interest Rate: 5.5%')
        
class ICIC(bank):
    def interest(self):
        print('ICIC interest Rate: 6.9%')
        
banks = [SBI(), HDFC(), ICIC()]

for j in banks:
    j.interest()
    
    
