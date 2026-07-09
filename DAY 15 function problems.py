#example:
nums = [23, 4, 6, 23, 7, 4]
empty = []
def removes_(nums, empty):
    for j in nums:
        if j not in empty:
            empty.append(j)
    print(empty)
removes_(nums, empty)

#example:
prime = 7
count = 0
def prime_not(prime, count):
    for i in range(1, prime+1):
        if prime % i == 0:
            count += 1
    if count == 2:
        print("prime number")
    else:
        print("not prime")
prime_not(prime, count)

#example:
some = "python is a programming language"
def counting(some, count):
    so = some.split(' ')
    for j in so:
        count += 1
    print(count)
counting(some, count)

#example:
some = "Pyhton Is a ProGraMming LanGuagE"
cap_count = 0
small_count = 0
space_count = 0
def cap_small(some, cap_count, small_count, space_count):
    for i in some:
        if i.isupper():
            cap_count += 1
        elif i .islower():
             small_count += 1
        else:
            space_count += 1
    print(f"there total{cap_count} number cap")
    print(f"there total{small_count} number small")
    print(f"there total{space_count} number spaces")
cap_small(some, cap_count, small_count, space_count)
