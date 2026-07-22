''' ------------FILE HANDLING--------------
file handling is an object that gives more options like creating, updating
two ways to open the file..
1.open()
-------
syntax
------
do = open('file_name', 'mode'):
     close()
2.with keyword
--------------
syntax
------
with open ('file_name', 'mode')as do:

with open('vinod.txt', 'r')as do:
    print(do.read())
     
modes:
r-----> used to read the file, incase if the file is not present it will raise error
w-----> used to write the text inside the file and it will ovverride the text inside file
'''
#eg:
with open ('vinod.txt', 'w')as do:
    print(do.write("we are using file handling"))
# a ---> this is used to add the text at last position inside the file    
    

with open ('v.txt', 'w')as do:
    print(do.write("vinod is a good boy"))

    
