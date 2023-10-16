'''
A Python dictionary is a collection of key-value pairs where each key is associated with a value.

A value in the key-value pair can be a number, a string, a list, a tuple, or even another dictionary. 
In fact, you can use a value of any valid type in Python as the value in the key-value pair.

A key in the key-value pair must be immutable. In other words, the key cannot be changed, for example, a number, a string, a tuple, etc.

Python uses curly braces {} to define a dictionary. Inside the curly braces, you can place zero, one, or many key-value pairs.
'''

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}
print(person['first_name'])
print(person['last_name'])


person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

ssn = person.get('ssn')
print(ssn)


'''
If the key doesn’t exist, the get() method returns None instead of throwing a KeyError. Note that None means no value exists.

The get() method also returns a default value when the key doesn’t exist by passing the default value to its second argument.
'''

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

ssn = person.get('ssn', 'default value')
print(ssn)


# Adding new key-value pairs

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

person['gender'] = 'Famale'

person['age'] = 26

print(person)

# Removing key-value pairs

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

del person['active']
print(person)


# Looping all key-value pairs in a dictionary
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

print(person.items())


for key, value in person.items():
    print(f"{key}: {value}")


# Looping through all the keys in a dictionary
for key in person.keys():
    print(key)


# Looping through all the values in a dictionary
for value in person.values():
    print(value)


'''
1. A Python dictionary is a collection of key-value pairs, where each key has an associated value.
2. Use square brackets or get() method to access a value by its key.
3. Use the del statement to remove a key-value pair by the key from the dictionary.
4. Use for loop to iterate over keys, values, and key-value pairs in a dictionary.
'''