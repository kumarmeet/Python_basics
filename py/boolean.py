"""
To represent true and false, Python provides you with the boolean data type. The boolean value has a technical name as bool.

The boolean data type has two values: True and False.

Note that the boolean values True and False start with the capital letters (T) and (F).
"""

is_active = True
is_admin = False

print(bool("Hello"))
print(bool(""))
print(bool(" "))

"""
Falsy and Truthy values
When a value evaluates to True, it’s truthy. And if a value evaluates to False, it’s falsy.

The following are falsy values in Python:

The number zero (0)
An empty string ''
False
None
An empty list []
An empty tuple ()
An empty dictionary {}

The truthy values are the other values that aren’t falsy.
"""

print(bool([]))
print(bool(None))
print(bool(()))
print(bool({}))