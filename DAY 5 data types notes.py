'Dictionary'
#Dict is a key :value pair separated by: , and keys are unique
#in the place of keys we have to use immutable data type..

'METHODS'
 
#1.KEYS()
#used to get all the keys from the dict(LHS of :)
#syntax: variable_name.keys()
#eg:
details={"Name" :"vinod",
         "Age" : 22,
         "Gender" : "Male"
         }
print(details.keys())
  

#2.VALUES()
#used to get all the keys from the dict(RHS of :)
#syntax:variable_name.values()
#eg:
details={"Name" :"vinod",
         "Age" : 22,
         "Gender" : "Male"
         }

print(details.values())
print(details.items())
 

 #3.ITEMS()
#used to get all the keys from the dict(arranges each line separetly in a tuple)
#eg:
details={"Name" :"vinod",
         "Age" : "22",
         "Gender" : "Male"
         }
print(details.items())


#4.clear()
#used to clear all the details in variable
#eg:
details={"Name" :"vinod",
         "Age" : "22",
         "Gender" : "Male"
         }
print(details.clear())
 

#5.update()
#used to update  the details in variable
#eg:
details={"Name" :"vinod",
         "Age" : "22",
         "Gender" : "Male"
         }
print(details.update({"mob" : "234566"}))


'SETS'

#Set is a collection of elements separated by ,
#set is muttable
#can remove duplicate value by itself


'Methods'
 
#1.Union-->(|)
#combine the values in the both sets
#syntax--> set1.union(set2) set1 | set2
#eg:
go={1,2,3}
so={4,5,6}
print(go.unoin(so))

#2.intersection()
# -->gives common elements from the sets
#syntax--> set1.intersection(set2)
#eg:
go={1,2,3,4}
so={4,5,6}
print(go.intersection(so))

#3.Symmetric_difference()
#removes common values and prints values in an order
#eg:
go={1,2,3}
so={4,5,6}
print(go.Symmetric_difference(so))
print(go ^ so)
    
#4.add()
#used to add new value
#syntax:variable_name.add()
#eg:
go={1,2,3}
go.add(7)
print(go)

#5.pop()
#used to delete element based on index.if not declared deletes last element.
#eg:
go={1,2,3}
go.pop(7)
print(go)

#6.discard()
#used to remove element but doesnt print error if the given value is not in the set.

#eg:
go={1,2,3}
go.discard(2)
print(go)
