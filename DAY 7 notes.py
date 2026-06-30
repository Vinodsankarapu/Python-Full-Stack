'input formatting from user'
#input():
#---> The input() function is used to takr input from the user..

#1 int:
num = int(input("enter a number:"))
num_2 = int(input("enter a number:"))
print(num + num_2)

#2 string:
#eg:
how = input("enter a char:")
print(how + "vinod")

#3 float:
#eg:
num = float(input("enter a number:"))
print(num)

#4 list:
#eg:
group = list(map(int, input().split()))
print(group)

#5 tuple:
#eg:
group = tuple(map(int, input().split()))
print(group)

#eg:
group = tuple(input().split())
print(group)

# f string:is a way to insert variables or expressions directly into a string by using an f before the string and placing values inside curly braces {}.
#eg:
name = input("enter your name: ")
age = int(input("enter your age: "))
print(f"{nane} your age is{age}")

#eg:
name = input("enter your name: ")
marks = int(input("enter your marks: "))
print(f" my name is {name}and my marks is{marks}")

#eg:
name  = input("enter your name: ")
age = int(input("enter your age: "))
print("my name is %s and i am %d years old %(name , age)
          
            
          


             


                  
