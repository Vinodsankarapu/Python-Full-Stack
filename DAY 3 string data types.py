""" DATA TYPES:
---> Data type defines kind os value a variable can store"""
# int
ex : num = 8

# float
ex: num = 65.89

# string:
---> #string is a sequence of the characters that enclosed in ', ", " " is called string
----> #sting is a unmutable 
ex: name = "vinod"

# indexing:
---->  #this is used to access the particular char in the string by pass insex position value.
----> #index start from 0
----> #we have negative indexing to count postion from last to first.
ex: so = "python is a language"
print(so[12])
print(so[-3])

# string methods:
1) #replace()
---> #this method is used to change any substring in that particular string.
# syntax--> variable_name.replace("old string", "new string", count)
ex: so = "python is a language"
print(so.replace("python", "java"))
print(so.replace("a", "A"))

2) #join()
----> #this method used to add new substring after each char in the string.
# syntax---> "string".join (variable_name)
ex: words = ["Python", "Full", "Stack"]

result = "-".join(words)

print(result)


3) #split()
---->#this string can be divide the string into different index into list, based on the string by pass by us..
# syntax---> "variable_name.split())
so = "python is a language:
print(so.split("is"))

4) #count()
---> #used to count the substring in the particular string and also specify the index postion.
# syntax ---> variable_name.count("substring", start index, ending index)
ex: so = "python is a language"
print(so.count("a"))

# string bulit in function
#len()
---> #this will find the length of the string, which is number char present in that string
eg: so = "python is a lamguage"
print(len(so))

# max()
---> # we will get max char in the string
eg: so = "python is a language"
print(max(so))

# min()
---> # we will get min char in the string
eg: so = "python is language"
print(min(so))
    

    




