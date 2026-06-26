""" list data types"""

#----> list is a collection of different data types that are enclosed in [] separeted by (commas,)
# list is a muttable
all_type = [1, 'python', [1, 2]]
for j in all_type:
    print(j)
#methods:: 1.append() 2.extend() 3.pop() 4.remove() 5.insert()
 # append():
 #--->it used add new item into list, bit it will add in the last index postion   
#ex:
any = [1, 2, 3,4]
print(any)
any.append(5)
print(any)

# extend():
#---> this is also add a item in the last index position, but it will give each value in the each index position.
#eg:
any = [1, 2, 3, 4]
any.extend("python")
print(any)

# index():
any = [1, 2, 'python is a language', [45, 78, "java is a language", [1, 23], 90], "hello"]
print(any[3])

# pop():
#----> used to delete the value from the list, but it will delete based on the index postion value.
#eg:
any = [1, 2, 3, 4, 98, 67]
any.pop(3)
print(any)

#mutable                                                        #immutable
#---> the data type can be modified                             #---> can't be modified
any = [1, 2, 3, 4]                                              
any.append(5)
print(any)
                                                                 
