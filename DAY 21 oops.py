''' self keyword
----------------
---> self refers to current object...
'''
class test:
    def display(self):
        print(self)
te = test()
print(te)
te.display()
        
''' constructor
--------------
---> this constructor initializes the object automatically when it is created....
'''
class Batch:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch
    def display(self):
        print(self.name)
        print(self.branch)
B1 = Batch(name="vinod", branch="AIDS")
B1.display()

class fam:
    def __init__(self):
        self.name = "vinod"
f = fam()
print(f.name)

#outside the class(private):
class bank:
    def __init__(self):
        self.__pin = "6600"
ac = bank()
print(ac._bank__pin)

#inside the class (public):
class bank:
    def __init__(self):
        self.__pin = "7700"
    def display(self):
        print(self.__pin)
a1 = bank()
a1.display()

'''Encapsulation
----------------
---> means wrapping the data and methods into a single unit(class) while controlling acces to the data
'''
class atm:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(self.__balance)
tran = atm(balance = int(input("enter amount: ")))
tran.deposit(amount = int(input("enter deposit: ")))
           
        
        
    
