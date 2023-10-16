numbers = [1, 3, 2, 7, 9, 4]
print(numbers[-1])
print(numbers[-2])
print(numbers[0])
print(numbers[4])

numbers.append(100)

print(numbers)


numbers.insert(2, 405)

print(numbers)


del numbers[0]

print(numbers)


last = numbers.pop()

print(last)
print(numbers)


second = numbers.pop(1)

print(second)
print(numbers)

numbers.remove(9)
print(numbers)


'''
1. A list is an ordered collection of items.
2. Use square bracket notation [] to access a list element by its index. The first element has an index 0.
3. Use a negative index to access a list element from the end of a list. The last element has an index -1.
4. Use list[index] = new_value to modify an element from a list.
5. Use append() to add a new element to the end of a list.
6. Use insert() to add a new element at a position in a list.
7. Use pop() to remove an element from a list and return that element.
8. Use remove() to remove an element from a list.
'''