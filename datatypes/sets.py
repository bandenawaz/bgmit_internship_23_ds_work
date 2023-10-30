'''
SET:
    A set is an unordered and unindexed collection of items.
    It is collection of data type which is mutable, iterable,
    and does not contain duplicate values.
'''

#lets define a set
universe = {'GOOG','AAPL','NFLX','GE'}
print(universe)

#lets add elements to the set
universe.add('AMZN')
print(universe)

#lets test for duplicates
universe.add('GOOG')
print(universe)

#lets add a list of items to the set
universe.update(['FB', 'TSLA'])
print(universe)

#lets find the length of the set
print(len(universe))

#lets delete an element from the set
universe.remove('FB')
print(universe)

universe.discard('TSLA')
print(universe)

