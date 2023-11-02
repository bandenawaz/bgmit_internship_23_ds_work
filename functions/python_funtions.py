'''
Functions:
    A function is a block of code that that performs a specific
    tasks and runs only when called 


def greet():
    """Function to greet people"""
    print("Hello!, Namaste Trump")

greet()
'''
#task: wap to find out the factorial of given number
#To check whether the number is palindrome or not


''' Parameterized function'''
'''
def greetPerson(person):
    """Function to greet a specific person"""
    print("Howdy!", person)

name = input("Enter the name of the person")
greetPerson(name)

def addNumber(a,b):
    return a + b
#define other functions

x = int(input("Enter the first number"))
y = int(input("Enter the second number"))

print("The sum of the numbers is ", addNumber(x))
#print the functions individually


#functions with default values
def exp(a,b = 3):
    return a**b

x = int(input("Enter the number"))
print(exp(x, 5))
'''
'''
Lambda functions
        These are quicker ways to write a function on the fly
        or on a single line. They are also called as anonymous functions
    
    syn: lambda argument : expression
'''

s = lambda a : a * a

x = int(input("Enter the number"))
print("Square of {0} is {1}".format(x, s(x)))

#WAP to find max of two numbers using lambda function
g = lambda a,b : max(a,b)
h = lambda a,b : a if(a > b) else b

d = int(input("Enter the first number"))
e = int(input("Enter second number"))

print("The max of two numbers is ",h(d,e))
