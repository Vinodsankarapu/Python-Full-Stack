






'''
2.search()
---------
----> ths search() will find the char, but it will the first sequence that found in the string...

3.split()
--------
4.sub()
-------
5.fullmatch()
-------------
metachar()
---------
[]
^
$
.
*
+
{}

'''
import re
txt = 'python is a language and also called dynamically typed'
print(re.search('[a]', txt))

import re
txt = 'python is a language and also called dynamically typed'
print(re.split(' ', txt))

import re
txt = 'python is a language and also called dynamically typed'
print(re.sub(' ', '&', txt))

import re
txt = 'I have 100 Rupee'
print(re.findall('[0-9]', txt))
print(re.findall('[a-z]', txt))
print(re.findall('[A-Z]', txt))

print(re.search('[0-9]', txt))
print(re.findall('[a-z]', txt))
print(re.findall('[A-Z]', txt))



