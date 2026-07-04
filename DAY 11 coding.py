#example: -->palindrom:
so = "vinod"
empty = ""
for i in so:
    empty = i + empty
if empty == so:
    print(f"{so} palindrom")
else:
    print(f"{so} is not a palindrom")

so = input("enter a word: ")
say = so[::-1]
if say == so:
    print("palindrom")
else:
    print("not palindrom")
    
# example fabinoc series:
num = 0
num_2 = 1
limit = int(input("enter a number: "))
print(num, num_2, end=" ")
for i in range(1, limit+1):
            all = num + num_2
            num = num_2
            num_2 = all
            print(all, end=" ")
# example calculator:
val_1 = int(input("enter a number: "))
val_2 = int(input("enter a number: "))
user_in = int(input("enter \n1.add \n2.sub \n3.mul \n4.pow:  "))
if user_in == 1:
   print(val_1 + val_2)
              
elif user_in == 2:
    print(val_1 - val_2)
elif user_in == 3:
    print(val_1 * val_2)
else:
    print(val_1 ** val_2)

#  table example:
num = 19
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# prefect number example:
num = int(input("enter a number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum += i
if sum == num:
    print(f"{num} is a prefect number")
else:
    print(f"{num} is a not a prefect number")



    
    
    


            
            
