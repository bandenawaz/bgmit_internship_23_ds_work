'''
List Comprehensions:
    Its an elegant way to define and create a list in Python.
    It is used to create a list from another sequence, jut like
    mathematical set notation in a single line.

    syn: [output_expression iterator expression conditional statement]

'''

#traditional list
cube_list = []

for i in range(1,10):
    cube_list.append(i**3)

print(cube_list)

#using list comprehension
cube = [i**3 for i in range(1,10)]
print(cube)

#task: print all the numbers which are divisible by 6 between 0 and 100
print([i for i in range(1,100) if(i%2==0) if(i%3==0)])

#lets segregate a list of numbers into Even and Odd numbers
print([str(i) + ': Even' if(i%2==0) else str(i) + ':Odd'  for i in range(1,20)]  )