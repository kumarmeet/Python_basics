price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

net_price = float(price) * float(tax) / 100

print(f'The net price is ${net_price}')

"""
Besides the int(str) functions, Python support other type conversion functions. 
The following shows the most important ones for now:

float(str) - convert a string to a floating-point number.
bool(val) - convert a value to a boolean value, either True or False.
str(val) - return the string representation of a value.

To get the type of a value, you use the type(value) function.
"""