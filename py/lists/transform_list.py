# When working with a list (or a tuple), you often need to transform the elements of the list and return a new list that contains the transformed element.

def double(bonus):
    return bonus * 4


bonuses = [100, 200, 300]

iterator = map(lambda b: b * 2, bonuses)
iterator = map(double, bonuses)

'''
Once you have an iterator, you can iterate over the new elements using a for loop.
Or you can convert an iterator to a list by using the the list() function:
'''
ls = list(iterator)
print(iterator)
print(ls)

names = ['david', 'peter', 'jenifer']
new_names = map(lambda name: name.capitalize(), names)
print(list(new_names))


carts = [['SmartPhone', 400],
         ['Tablet', 450],
         ['Laptop', 700]]

TAX = 0.1


carts = map(lambda item: [item[0], item[1], item[1] * TAX], carts)
print(list(carts))

def calc(item):
    print("444",item)
    return [item[0], item[1], item[1] * TAX]

cartsr = map(calc, carts)
print(list(cartsr))

# Use the Python map() to call a function on every item of a list and returns an iterator.