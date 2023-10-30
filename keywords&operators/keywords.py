'''
Keywords:
        Keywords are reserved words in Python. They are built into core language.
        They cannot be used as a variable name, class name, function name or any
        other identifier.

        These keywords are used to define the syntax and semantics of Python.
'''

'''
and: This is a logical operator used to combine conditional statements
and returns true if both statements are true, else false.
'''
print((5 > 3) and (4 > 2))

'''
as: This is used to create an alias.

'''
import calendar as cal

print(cal.isleap(2023))
print(cal.isleap(2024))
print(cal.month_name[8])

'''
asset: 
        It is used while debugging code. It allows us to check if a condition
        in code returns true, if not Python will raise an assertion error.
'''
stock = 'GOOG'
assert stock == 'GOOG'

assert stock == 'NVDA'