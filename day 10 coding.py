"""Genearting the prime Number"""
#example:
num =int(input("Enter a Number:"))
count=0 # It count the Number
for j in range(1,num+1): #(1,2,3,4,5,6,7)
    if num % j == 0: #(7%1==0,7%2==0,7%3==0,7%4==0)
        count+=1 #It count the number (5)
if count == 2: #7==2
    print(f"{num} is a prime")
else:
    print(f"{num} not prime")
    
#example:
limit_= 20
for j in range(1,limit_+1):
    count=0 #Becasue we limit the count
    for i in range(1,j+1):
        if j % i ==0:
            count +=1
    if count == 2:
        print(f"{j} is a prime")
        
#example:
num = 5
for j in range(1,num+1):
    for i in range(1,j+1):
        print("*",end = " ")
    print()
        
#example:
num = 5
for j in range(1,num+1):
    for i in range(1,j+1):
        print(j,end = " ")
    print()
    
#example:        
num = 5
for j in range(1,num+1):
    for i in range(1,j+1):
        print(i,end = " ")
    print()
    
#example:
num = 5
count =0
for j in range(0,num+1):
    for i in range(1,j+1):
        count+=1
        print(count,end = " ")
    print()
    
#example:
num = 4
count =0
for j in range(num,0,-1):
    for i in range(1,j+1):
        count +=1
        print(i,end = " ")
    print()

#Arm strong:The number and total length of the number is power that number is equal to numbers is called arm strong:
#example:    
am_stg = 153 
length = len(str(am_stg))
all_sum =0
for j in str(am_stg):
    all_sum +=int(j)** length
if all_sum == am_stg:
    print(f"{am_stg} is amstrong")
else:
    print(f"{am_stg} is not amstrong")

#example:
num =5
for j in range(num):
    print(" " *(num-j-1),end = " ")  
    print("*" *(2 * j + 1)) 
