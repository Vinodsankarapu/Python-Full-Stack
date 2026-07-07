'''passing by value'''
def some(a):
    for j in a:
        print(j)
some((1, 2, 3, 4, "python"))

'''reference'''
a = (1, 2, 3)
def some(a):
    for j in a:
        print(j)
some(a)
'''retutn keyword
---> in a function if a return is executed then it will exit from the function with certain returned values'''
#eg:
def myfunc_(b):
    return 5 + b
a = myfunc_(10)
c= myfunc_(100)
print(a)
print(c)

import builtins

builtin_functions = [
    name for name in dir(builtins)
    if callable(getattr(builtins, name))]
print(builtin_functions)
print(f"total built-in functions are (len(builtin_function))")



'''Recursive Function
                                   
---->Recursive function that calls itself repeatedly until a specified condition is met..    
syntax:
def func_name(parameter):
    if condition: --> base case
        return statement
    else:
         retrun statement
print(fun_name(argumrnts))'''

                                
def func_name(num):
    if num == 1:
        return 1
    else:
        return num * func_name(num-1)
a = func_name(5)
print(a)
    


