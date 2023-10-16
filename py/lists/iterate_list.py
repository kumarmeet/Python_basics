# Using Python for loop to iterate over a list

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for city in cities:
    print(city)


# Using Python for loop to iterate over a list with index

'''
Sometimes, you may want to access indexes of elements inside the loop. In these cases, you can use the enumerate() function.
The enumerate() function returns a tuple that contains the current index and element of the list.
'''
for item in enumerate(cities):
    print(item)


cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for index, city in enumerate(cities):
    print(f"{index}: {city}")


cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for index, city in enumerate(cities,1):
    print(f"{index}: {city}")

# The rule of thumb is that if you know if can loop over something, it’s iterable.

colors = ['red', 'green', 'blue']
colors_iter = iter(colors)

color = next(colors_iter)
print(color)


'''
1. Use a for loop to iterate over a list.
2. Use a for loop with the enumerate() function to access indexes.
'''