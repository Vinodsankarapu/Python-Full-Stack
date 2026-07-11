"""
----------------------------Modules--------------------------------------
--> A Module is a python file (.py) that contains reusable code
1.Varibles
2.Functions
3.Classes
4.Objects
5.Statements

Why this
--------
-->Insead of writing the same code repatedly, we can store it in a module
and use it whenever needed
Types of Modules
1.user- define
2.Bulit-in
-> math
sqrt() ---> square root
factorial() ---> factorial
pow() ---> power
cell() --> roundup
pi() ---> pi value
-> os
---> the os module is used to interact with operating system
-> sys
---> this will provide the information about python interpeter
import sys
print(sys.version)
-> random
---> used to generate random values

"""
import vinod
print(vinod.add(5,3))
print(vinod.sub(5,3))
print(vinod.mul(3, 4))
print(vinod.pow(2, 3))


" import specific function"
from vinod import add, sub
print(vinod.add(2, 5))
print(vinod.sub(10, 3))

# usins alias name:
import vinod as m
print(m.mul(2, 4))

import math
print(math.sqrt(25))
print(math.factorial(4))
print(math.pow(2, 5))

import os
print(os.getcwd()) # current dictionary
os.mkdir("hii") # create a new floder
os.rmdir("hii") # remove

import random
print(random.randint(1000, 9999))

colors = ["yellow", "red", "blue", "green"]
print(random.choice(colors))
