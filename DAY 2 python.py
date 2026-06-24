"""OPERATORS:
.....
1)Arithmetic operator 
2)Assignment operator 
3)Comparision operator
4)logical operator
5)Identity operator
6)Membership operator
7)Bitwise operator """

#1)arithmetic operator : +, -, *, /, % 
a = 30
b = 20
print(a+b) # addition
print(a-b) # subtraction
print(a*b) # multiplication
print(a /b) # division
print(a%b) # module

#2)assignment operator : =, +=, -=, *= %=
a = 10
a += 5
print(a)

a = 20
a -= 5
print(a)

b = 20
b *= 2
print(b)

a = 10
a %= 2
print(a)

#3) comparision operator: <, >, <=, >=, !=, ==
a = 20
b = 15
print(a > b)
print(b < a)
print(a >= b)
print(b <= a)
print(a != b)
print(a == a)

#4) logical operator: AND, OR, NOT
a = 20
b = 30
print (a>10 and b<40)
print(a<15 or b>25)
print(not(a == b))

#5) identity operator: is, isnot
===> is operator are used same object
===> is not operator are used notsame object
a = 20
b = 20
print(a is b)

a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)

a = 20
b = 20
print(a is not b)

a = 20
b = 10
print(a is not b)

#6) member ship operator: in not in
==> in operator are used value present
===> not in operator are used notvalue present
numbers = [10, 20, 30, 40]
print(20 in numbers)
print(50 not in numbers)"""

















