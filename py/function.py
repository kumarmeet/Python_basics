'''
1. A Python function is a reusable named block of code that performs a task or returns a value.
2. Use the def keyword to define a new function. A function consists of function definition and body.
3. A function can have zero or more parameters. If a function has one or more parameters, you need to pass the same number of arguments into it.
4. A function can perform a job or return a value. Use the return statement to return a value from a function.
'''

def greet(name):
    return f"Hi {name}"

print(greet("Sam"))


# Default params

# works -> def function_name(param1, param2=value2, param3=value3, ...):
# can not work -> def function_name(param1=value1, param2, param3):

def greet(name, message='Hi'):
    return f"{message} {name}"

print(greet("Meet"))


'''
Use Python default parameters to simplify the function calls.
Place default parameters after the non-default parameters.
'''

# Python Keyword Arguments

def get_net_price(price, tax=0.07, discount=0.05):
    return price * (1 + tax - discount)

net_price = get_net_price(100, 0.06)

print(net_price)

# net_price = get_net_price(100, tax=0.08, 0.06) (error)

net_price = get_net_price(price=100, discount=0.06)
print(net_price)

'''
1. Use the Python keyword arguments to make your function call more readable and obvious, especially for functions that accept many arguments.
2. All the arguments after the first keyword argument must also be keyword arguments too.
'''


# Python Lambda Expressions

'''
Python lambda expressions allow you to define anonymous functions.

Anonymous functions are functions without names. The anonymous functions are useful when you need to use them once.

A lambda expression typically contains one or more arguments, but it can have only one expression.
'''

# lambda parameters: expression

def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)

def first_last(first_name, last_name):
    return f"{first_name} {last_name}"


def last_first(first_name, last_name):
    return f"{last_name}, {first_name}"


full_name = get_full_name('John', 'Doe', first_last)
print(full_name) # John Doe

full_name = get_full_name('John', 'Doe', last_first)
print(full_name) #  Doe, John

# OR

full_name = get_full_name('John', 'Doe', lambda first_name, last_name: f"{first_name} {last_name}")
print(full_name) # John Doe

full_name = get_full_name('John', 'Doe', lambda first_name, last_name: f"{last_name} {first_name}")
print(full_name) #  Doe, John

def times(n):
    return lambda x: x * n

double = times(2)

result = double(2)
print(result)

result = double(3)
print(result)


#lambda in a loop

callables = []
for i in (1, 2, 3):
    callables.append(lambda a = i: a)

for f in callables:
    print(f())


'''
Use Python lambda expressions to create anonymous functions, which are functions without names.
A lambda expression accepts one or more arguments, contains an expression, and returns the result of that expression.
Use lambda expressions to pass anonymous functions to a function and return a function from another function.
'''


# Python Function Docstrings

def add(a, b):
    "Return the sum of two arguments"
    return a + b

help(add)


def add(a, b):
    """ Add two arguments
    Arguments:
        a: an integer
        b: an integer
    Returns:
        The sum of the two arguments
    """
    return a + b

help(add)


'''
1. Use the help() function to get the documentation of a function.
2. Place a string, either single-line or multi-line strings, as the first line in the function to add documentation to it.
'''