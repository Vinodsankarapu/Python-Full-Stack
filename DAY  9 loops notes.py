''' LOOPS'''

#1) for loop:---> a for loop is used to iterate  over a sequence, list, tuple, dict

#eg: string
any = "python is a language"
for j in any:
    print(j)
    
# eg: list
any = [1, 2, 3, 4, 5]
for j in any:
    print(j)
    
# eg: tuple
for j in any:
    print(j)
    
# eg: dictionary
any  = {"name": "vinod",
        "role": "student"}
for j in any.values():
    print(j)

'''else in for loop:the else block wiil be excuted the for loop but in case the loop is breaked'''
#eg:
any = [1, 2, 3, 4]
for j in any:
    print(j)
else:
    print("end")


''' RANGE():----> range() it is an built in function that is used to generate a squence upto a limit
syntax---> range(start, end, step)'''
#eg:
for j in range(1, 11):
    print(j)

'''WHILE LOOP:---> the while loop will executed untill the condition becomes true...'''
# eg:
i = 1
while i <= 5:
    print(i)
    i += 1

# eg:
i = 1
while i <= 5:
    print(i)


''' CONTROL STATEMENTS

1)BREAK:---> the break is used to exit for the loop'''
# eg:
any = [1, 2, 3, 4, 5]
for j in any:
    print(j)
    if j == 3:
        break
# eg:
any = [1, 2, 3, 4, 5]
for j in any:
    print(j)
    if j == 3:
        break
    else:
        print("end")


'''CONTINUE: ---> the continue will skip the current iteration'''
# eg:
any = [1, 2, 3, 4, 5]
for j in any:
    if j == 2:
        continue
    print(j) 

''' ASSERT KEYWORD:
---> it will used to check the condition, but it will raise an error incase it is false...raise the error'''
# eg:
age = int(input("enter a age: ")
assert age>= 18, "eligable for vote"          
    

