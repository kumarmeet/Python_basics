'''
A dictionary comprehension allows you to run a for loop on a dictionary and do something on each item like transforming or filtering and returns a new dictionary.

Unlike a for loop, a dictionary comprehension offers a more expressive and concise syntax when you use it correctly.

{key:value for (key,value) in dict.items() if condition}
'''

stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}


# Using Python dictionary comprehension to transform a dictionary
new_stocks = {}
for symbol, price in stocks.items():
    new_stocks[symbol] = price*1.02

print(new_stocks)


'''
First, loop over the items of the stocks dictionary
Second, increase the price by 2% and add the item to the new dictionary (new_stocks).
'''
new_stocks = {symbol: price * 1.02 for (symbol, price) in stocks.items()}

print(new_stocks)


# Using Python dictionary comprehension to filter a dictionary

selected_stocks = {}
for symbol, price in stocks.items():
    if price > 200:
        selected_stocks[symbol] = price

print(selected_stocks)


selected_stocks = {s: p for (s, p) in stocks.items() if p > 200}

print(selected_stocks)

# A dictionary comprehension iterates over items of a dictionary and allows you to create a new dictionary by transforming or filtering each item.
