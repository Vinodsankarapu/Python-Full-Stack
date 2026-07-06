'''FUNCTIONS
---> function is a block of code can be reusable
---->function can avoid the repeated line of code
function of 2 types:
1) built in function
eg ---> print(), max(), type(), min(), sum()

2) user-define:
----> this function startsn with a keyword (def)
def func_name(parameters):
   ------------
   -----------
   -----------
func_name(arguments)'''

#eg:
def add():
    print("helli")
add()

#eg:
def add(a, b):
    print(a +b)
add(10, 20)

''' types of arguments:
1.Required arguments
----> we have to pass  same number arguments with defination of the function
2.Default arguments
3.keyword arguments
----> we can pass as a pair like)(variable = datatype)
4.variable length
---> we can pass n nnumber of arguments and just using (args*) in the parameter wiil recieve tuple of arguments'''

#required arguments:
# pass to the same number of required arguments
def add(a, b):
    print(a+b)
add(2)

#keyword:
def add(a, b):
    print(a + b)
add(a=4, b=9)

# default:
num = 7
num_2 = 9
num_3 = 8
def add(a, b, c):
    print(a)
    print(b)
    print(c)
add(num, num_2, num_3)

#variable length (* args):
num = 7
num_2 = 9
num_3 = 8
def add(*a):
    print(a)
add(num, num_2, num_3)

# another example:
num = 7
num_2 = 9
num_3 = 8
def add(*a):
    print(a[1])
add(num, num_2, num_3)

num = 7
num_2 = 9
num_3 = 8
num_4 = "python"
def add(*a):
    print(a)
add(num, num_2, num_3, num_4)

#eg (**args):
def all(** any):
    print(any['age'])
all(name = "vinod", age = 21)

"global variabel: ---> variable that is declared outside of the functions"
#eg:
num = 9
def func():
    print(num)
func()

'''change the global variable  by using keyword (global) that can change completely inside and outside of the function''':
#eg:
num = 9
def fun():
    global num
    num = 89
    print(num)
fun()
print(num)
    

"local variable: ---> variable that is declared only inside of the function"
#eg:
def fun():
    num = 9
    print(num)
fun()    
    


