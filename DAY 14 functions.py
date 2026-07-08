''' lambda function
----> this is also called as annonymous function.
----> A lambda function can take n number of arguments but having only one expression

syntax ---> lambda arguments : expression
'''
#eg:
some = lambda an: an+5
print(some(10))

#eg:
some = lambda an: an *5
print(some(2))

#eg:
some = lambda an, so: an - so
print(some(20, 10))

''' filter()
---> the filter() function is a built-in function used to filter elements from an itterable such as list, tuple and set based on condition
syntax ---> filter(function, itterable)

---> this filter() function returns filter object so we can convert that into other types list, tuple, and list'''
#eg:
nums = [1, 2, 3, 4, 5]
rev = filter(lambda a: a%2 ==0, nums)
print(list(rev))

#eg:
nums = [1, 2, 3, 4, 5]
rev = filter(lambda a: a%2 !=0, nums)
print(set(rev))

''' list comprehension
----> this offers a shorter syntax when we want to create a new list from the old

syntax ---> variable_name = [expression loop condition]
'''
#eg:
old = [1, 2, 3, 4, 5, 6]
new = [j for j in old]
print(new)

#eg:
old = [1, 2, 3, 4, 5, 6]
new = [j for j in old if j %2 == 0]
print(new)
