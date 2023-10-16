numbers = [1, 2, 3, 4, 5]

squares = []
for number in numbers:
    squares.append(number**2)

print(squares)


numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda number: number**2, numbers))

print(squares)


'''
Since the map() function returns an iterator, you need to use the list() function to convert the iterator to a list.

Both the for loop and map() function can help you create a new list based on an existing one. But the code isn’t really concise and beautiful.

To help you create a list based on the transformation of elements of an existing list, Python provides a feature called list comprehensions.
'''

numbers = [1, 2, 3, 4, 5]
# [output_expression for element in list]
squares = [number**2 for number in numbers]

print(squares)


mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]


highest_mountains = list(filter(lambda m: m[1] > 8600, mountains))
print(highest_mountains)


highest_mountains = [x for x in mountains if x[1] > 8600]
print(highest_mountains)

'''
Python list comprehensions allow you to create a new list from an existing one.
Use list comprehensions instead of map() or filter() to make your code more concise and readable.
'''