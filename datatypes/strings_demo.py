'''
String: A string is collection of characters, numbers and other
characters written within a single or double quote.
'''

#Variable assignment using string
sample_string = '1% can also be expressed as 0.01'
print(type(sample_string), sample_string)

#In Python, anything that goes within the quotes , is interpreted as a string
stock_price = '224.61'
print(type(stock_price), stock_price)

#Lets concatenate Two Strings with + operator
print('The price of Apple Inc is ' + stock_price + '$')
sp = 224.61

#Lets concatenate String with Float
#print('The price of Apple Inc is ' + sp + '$')

#Lets print a name multiple times
print('Manojilla '* 3)
print('BGMIT EC Dept \n'*8)

'''
Slice:
    Extracting a substring from a string or part of a string fro a string is called
    as slicing.
    We use [] to perform the slicing

    Syn: string[index]
'''

ml = 'Machine Learning'
print(ml[8])

#lets print the length of the string
print(len(ml))

#To extract a substring from the string we use
#str[start index: end index]
print(ml[0:7])

#lets print just learning
print(ml[8:])

#just Mach
print(ml[:4])

#to step over indices we use str[start index: end index:step value]
print(ml[::2])

#Operations on String
#upper(): returns the upper case version of the string
ss = "machine learning"
print(ss.upper())

ssl = "MACHINE LEARNING"
#convert it to lower case
print(ssl.lower())

#strip: returns the string with whitespace removed
print('    A string with whitespace at both ends    '.strip())

#remove whitespace from the left side of the string
print('    A string with whitespace at both ends    '.lstrip())

#remove whitespace from the right side of the string
print('    A string with whitespace at both ends    '.rstrip())