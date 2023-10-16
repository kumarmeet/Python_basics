message = 'It\'s also a valid string'

print(message)


# Creating multiline strings

help_message = '''
Usage: mysql command
    -h hostname     
    -d database name
    -u username
    -p password 
'''

# f-strings

print(help_message)

name = 'John'

print(f'Helllo {name} {message}')


# concate strings

greeting = 'Good ' 'Morning!'
print(greeting)

greeting = 'Good '
time = 'Afternoon'

greeting = greeting + time + '!'
print(greeting)

# from start side
str = "Python String"
print(str[0])
print(str[1]) 

# fron end side
str = "Python String"
print(str[-1])
print(str[-8]) 

# length
str = "Python String"
str_len = len(str)
print(str_len)


# Slicing strings [start: end: steps]

str = "Python String"
print(str[0:2])

#strings are immutable

str = "Python String"
str[0] = 'J' # error


"""
1. In Python, a string is a series of characters. Also, Python strings are immutable.
2. Use quotes, either single quotes or double quotes to create string literals.
3. Use the backslash character \ to escape quotes in strings
4. Use raw strings r'...' to escape the backslash character.
5. Use f-strings to insert substitute variables in literal strings.
6. Place literal strings next to each other to concatenate them. And use the + operator to concatenate string variables.
7. Use the len() function to get the size of a string.
8. Use the str[n] to access the character at the position n of the string str.
9. Use slicing to extract a substring from a string.
"""