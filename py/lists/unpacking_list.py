# Introduction to the list unpacking

colors = ['red', 'blue', 'green']

# Python provides a better way to do this. It’s called sequence unpacking.
red, blue, green = colors

print(red, blue, green)


'''
Unpacking and packing
If you want to unpack the first few elements of a list and don’t care about the other elements, you can:

First, unpack the needed elements to variables.
Second, pack the leftover elements into a new list and assign it to another variable.
By putting the asterisk (*) in front of a variable name, you’ll pack the leftover elements into a list and assign them to a variable.
'''
colors = ['red', 'blue', 'green']
red, blue, *left_over = colors

print(red, blue, left_over)


'''
Unpacking assigns elements of the list to multiple variables.
Use the asterisk (*) in front of a variable like this *variable_name to pack the leftover elements of a list into another list.
'''