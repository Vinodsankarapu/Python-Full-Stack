""" TYPE CONVERSIONS"""
#----> This process of converting one data type to another data type.
# int:
#eg:
num =89
num_2 = float(num)
print(num_2)
print(type(num_2))
so = str(num)
print(type(so))
# float:string, integer
#eg:
num = 8.9
how = str(num)
print(how)
print(type(how))
num_2 = int(num)
print(num_2)
#string:integer, float, list, tuple
#eg:
hii = "678.9"
x = float(hii)
print(x)

# string into list:
any = "12345"
x = list(any)
print(x)

# string into tuple:
any = "12345"
x = tuple(any)
print(x)

#list:string, tuple, dictionary:
# list into string
var = ['p', 'y', 't', 'h', 'o', 'n']
text = "".join(var)
print(text)

# list into tuple
var = ['p', 'y', 't', 'h', 'o', 'n']
convert = tuple(var)
print(convert)

# list into dictionary
python = [('a', 1), ('b', 2)]
convert = dict(python)
print(convert)

# tuple: string, list:
# tuple into string
fam = ('h', 'e', 'l', 'l', 'o')
text_2 = "".join (fam)
print(text_2)

# tuple into list
fam = ['h', 'e', 'l', 'l', 'o')
convert = "".join(fam)
print(convert)

"""built in functions"""
# str()
# float()
# int()
# list()
# dict()
