#Define all the arithmetic functions
#addition
def addTwoNumbers(a,b):
    return a + b

#subtract two numbers
def subtractTwoNumbers(a,b):
    return a - b

#divide two numbers
def divideTwoNumbers(a,b):
    return a / b

#multiply two numbers
def multiplyTwoNumbers(a,b):
    return a * b

#modulo two numbers
def moduloTwoNumbers(a,b):
    return a % b

#raise power of two numbers
def raisePowerOfTwo(a,b):
    return a ** b

#floor division
def floorDivision(a,b):
    return a // b

#factorial of a number
def factorial(n):
    """Returns the factorial of a number"""
    i = 0
    result = 1
    while(i != n):
        i += 1
        result *= i
    return result 