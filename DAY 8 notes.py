'''Statements: They are Three Types COnditions,Control,Loop
condtions: if ifles elife
control:break continous,pass
loop:for while'''

#Conditions Statements:if,ifelse,elif
if:
num=10

if num%2==0:
    print(f"{num}is a Even")
    
#else:Else is the fall back statement in case the if condition is false then this else
num=int(input("Enter Your Number:"))

if num%2==0:
    print(f"{num}is a Even")
else:
    print(f"{num} is a odd")

#neasted if:If inside the if another equal to is called nested if
")

yogesh_ICIC_details ={"ATM PIN":'6600'}
pin_ = input("Enter your 4 digit ATM PIN: ")
if len(pin_)== 4:
    if pin_ in yogesh_ICIC_details['ATM PIN']:
        print("Welcome to ICIC ATM")
    else:
        print("You have Entered incorrct Pin")


#elif:It used in multiple conditions in one output
marks_ =int(input("Enter a NUmber:"))
if marks_>=90:
    print("A+")
elif marks_>=80:
    print("A")
elif marks_> 70:
    print("B+")
else:
    print("Fail")

2,control:break continous,pass
3,loop:for while



num=int(input("Enter Your Number:"))

if num%2==0:
    print(f"{num}is a Even")
else:
    print(f"{num} is a odd")

vinod_ICIC_details ={"ATM PIN":'6600'}
pin_ = input("Enter your 4 digit ATM PIN: ")
if len(pin_)== 4:
    if pin_ in yogesh_ICIC_details['ATM PIN']:
        print("Welcome to ICIC ATM")
    else:
        print("You have Entered incorrct Pin")

a="6600"
pin=input("Enter a Pin:")
if len(pin) == 4 and pin==a:
    print("Welcome to icc Atm")
else:
    print("You have Entered incorrct Pin")

#Marks
marks_ =int(input("Enter a NUmber:"))
if marks_>=90:
    print("A+")
elif marks_>=80:
    print("A")
elif marks_> 70:
    print("B+")
else:
    print("Fail")
    
#Vowel
a=input("Enter a Your Name:")
b="a,e,i,o,u,A,E,I,O,U"
if a in b:
    print("Vowel")
else:
    print("Consitent")
