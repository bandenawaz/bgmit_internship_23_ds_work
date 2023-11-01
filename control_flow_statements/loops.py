'''
Loops:
    Statements that keep executing within the given range
    or until the condition is met.

    1. while statement:
        It is used to repeat execution of the code or block of code
        that is controlled by an conditional statement or expression

        syn: while(condn):
                st1
                st2
                ....
                stn

dp = 6
count = 0

while(count != dp):
    print("Count: " , count)
    count += 1
else:
    print('Loop is terminated')

#Task: print all prime numbers between 1 and 100 using while
num = 1
while(num <= 100):
    count = 0
    i = 2

    while(i <= num//2):
        if(num % i == 0):
            count += 1
            break
        i += 1

    if(count == 0 and num != 1):
        print("%d" %num, end=' ')
    num += 1
'''
#task: write program to check the given number is palindrome or not


'''
for statement:
        The for statement in python is another looping technique
        which iterates over a sequence of objects
'''
ds = 'Data Science'
for d in ds:
    print('The word is :'+d)


#iterate over dictionary
myDict = {
    'AAPL': 193.64,
    'HP': 25.16,
    'MSFT': 1164.94,
    'GOOG': 1061.49
}

#lets iterate over dictionary
for key, value in myDict.items():
    print('The Price of {0} is {1}'.format(key,value))


'''
range function:
    It is used to generate a sequence or arithmetic progression
    which can be combined with for loop to repeat the code
    for the given range

    The default starting value is 0, default increment is 1 and 
    ends with specified number

    syn: range([start], stop,[step]) 
'''

for i in range(5):
    print(i)


#lets print an ap with 3 as increment between 1 to 50
for i in range(1,50,3):
    print(i, end=' ') 

#task: print multiplication table from 1-10
for i in range(1,11):
    print("Table of {0}".format(i))
    for j in range(1,11):
        print("{0} X {1} = {2}".format(i, j, i*j))
    print()
    