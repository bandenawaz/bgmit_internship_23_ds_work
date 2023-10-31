'''
Control Flow Statements
    The program's control flow is the order in which the program's
    code is executed or which control's the flow of execution of 
    the program.

    There are two kinds of flow statements
    1. Conditional flow statements
    2. Loop statements

    Conditional flow statements:
            In this case, the program will be executed only if the
            condition is true or met.
        a. if statement
        b. elif statement
        c. else statement

    if statement: 
        The if statement is used when we want a code to be executed
        under certain conditions. It can be either a single condition
        or multiple conditions.


x = int(input('Enter the first number'))
y = int(input('Enter the second number'))

if( x > y ):
    print("X is greater than Y")

print('Y is greater than X')
'''
'''
elif:
    This statement checks for the new condition and executes
    the code if they are held true after the conditions evaluated
    by the previous if statement weren't true
'''
x = int(input('Enter the first number'))
y = int(input('Enter the second number'))
z = int(input('Enter the third number'))

if( x > y and x > z ):
    print("X is greater ")
elif(y > z ):
    print('Y is greater ')
else:
    print('Z is greater')

print("I am executing from outside the condition")