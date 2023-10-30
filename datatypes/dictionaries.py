'''
Dictionary:
    A dictionary is an unordered collection of items, which
    stores the data in a key-value pair, separated by comma,
    and enclosed within curly brackets.

    Note: We can use only immutable objects like strings, numbers 
    or tuples for the keys of the dictionary, and keys of the dictionary
    should be unique.
'''

#lets create a empty dictionary
ticker = {}
print(ticker, type(ticker))

#lets create a dictionary using dict method
newTicker = dict()
print(newTicker, type(newTicker))

#lets create a dictionary with values
tickers = {
    'GOOG': 'Alphabet Inc',
    'AAPL': 'Apple Inc',
    'MSFT': 'Microsoft Corporation',
}
print(tickers, type(tickers))

#Create a dictionary with multiple data types
ticker = {
    'symbol': 'APPL',
    'price' : 224.96,
    'company': 'Apple Inc',
    'founded': 1976,
    'products': ['Machintosh','iPad','iPod','iPhone','airpods','iTv']
}
print(ticker)

#lets create nested dictionary
tick = {
    'AAPL': {
        'name': 'Apple Inc',
        'price': 224.96
    },
    'GOOG': {
        'name': 'Alphabet Inc',
        'price': 1194.6
    }
}
print(tick)

#lets check uniqueness of the key
same_key = {
    'symbol': 'AAPL',
    'symbol': 'GOOG'
}
print(same_key)

#Accessing the dictionary items
print("The price of Apple stock is ",ticker['price'])
print(ticker['products'])

#task: print iphone from product
print(ticker['products'][3])

print(tick['AAPL']['price'])

#Lets update the tick object with the new element
#called founders which is a list of founders
ticker['founders'] = ['Steve Jobs','Steve Woznaik','Ronald Wayne']
print(ticker)

#lets delete the item founders
del ticker['founders']
print(ticker)

#Dictionary Methods
'''
len(dictionary): It returns the length of the dictionary
'''
print(len(ticker))

'''
items(): It returns a tuple of key value pair
'''
print(ticker.items())

#lets print just keys
'''
keys(): It returns keys of the dictionary
'''
print(ticker.keys())