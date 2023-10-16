# The sort() method sorts the original list in place. It means that the sort() method modifies the order of elements in the list.

guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
guests.sort()

print(guests)


scores = [5, 7, 4, 6, 9, 8]
scores.sort(reverse=True)

print(scores)

'''
This sort_key() function accepts a tuple called company and returns the third element.

Note that the company is a tuple e.g., 
('Google', 2019, 134.81). And the company[2] references the revenue like 134.81 in this case.
'''


companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

def sort_key(company):
    return company[2]

# companies.sort(key=sort_key, reverse=True)
companies.sort(key=lambda comp: comp[2], reverse=True)

print(companies)


'''
1. Use the Python List sort() method to sort a list in place.
2. The sort() method sorts the string elements in alphabetical order and sorts the numeric elements from smallest to largest.
3. Use the sort(reverse=True) to reverse the default sort order.
'''


# sorted()

'''
As you can see clearly in the output, the original list doesn’t change. 
The sorted() method returns a new sorted list from the original list.
'''

guests = ['James', 'Mary', 'John', 'Patricia', 'Robert', 'Jennifer']
sorted_guests = sorted(guests)

print(guests)
print(sorted_guests)


scores = [5, 7, 4, 6, 9, 8]
sorted_scores = sorted(scores)

print(sorted_scores)

'''
1. Use the sorted() function to return a new sorted list from a list.
2. Use the sorted() function with the reverse argument sets to True to sort a list in the reverse sort order.
'''