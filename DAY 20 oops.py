"""
----------------oops---------------------------
code reusable
easy manintainece
clear understanding
better security

classess
--------
class is a bluprint or template used to create an object

class batch_4:
    pass
object
-----

object is a instance of the class

class yogesh:
    a="kumar"
kumar=vinod()
print(kumar)

attributes
---------
attributes are the varaiable that belongs to an object or the class
class how:
    def details(self,name,age):
        self.name=name
        self.age=age

s1=how()
s1.details('vinod',67)
print(s1.name)
print(s1.age)

Methods
--> Metohds are nothing but ,the functions inside class

class Calculator:
    def add(self,num,num2):
        print(num + num 2)
    def sub (self,num,num2):
        print(num - num2)
cal=Calculator()
cal.sub(78,9)

"""


"""class how:
    def details(self,name,age):
        self.name=name
        self.age=age
s1=how()
s1.details('vinod',22)
print(s1.name)
print(s1.age)

class n:
    a="vinod"
vinod=n()
print(vinod)

class vinod:
    a="varma"
    print(a)
n=vinod()"""

class Calculator:
    def add(self,num,num2):
        print(num + num2)
    def sub (self,num,num2):
        print(num - num2)
n=Calculator()
n.add(22,33)
n.sub(22,33)
