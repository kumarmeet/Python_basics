'''
Sometimes, you want to create a list of items that cannot be changed throughout the program. Tuples allow you to do that.

A tuple is a list that cannot change. Python refers to a value that cannot change as immutable. So by definition, a tuple is an immutable list.

Defining a tuple
A tuple is like a list except that it uses parentheses () instead of square brackets [].

'''

rgb = ('red', 'green', 'blue')

print(rgb)

print(rgb[0])
print(rgb[1])
print(rgb[2])


# Defining a tuple that has one element

numbers = (3, )
print(type(numbers))


'''
Assigning a tuple
Even though you can't change a tuple, you can assign a new tuple to a variable that references a tuple. For example:
'''

colors = ('red', 'green', 'blue')
print(colors)

colors = ('Cyan', 'Magenta', 'Yellow', 'black')
print(colors)