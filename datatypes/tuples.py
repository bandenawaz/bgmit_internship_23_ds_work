'''
Tuples:
    Tuples are the immutable data structures which contain
    heterogeneous sequence of elements separated by commas
    and enclosed within small brackets.
    The elements of the tuple are accessed through indexing 
    or unpacking.

'''

#lets create a tuple
tp = (1,2,3)
print(tp, type(tp))

#tuples with heterogeneous sequence of elements
tp2 = ('ML','DS','AI',56,98.99,5>6, 25//3)
print(tp2, type(tp2))

#creating tuples without braces
tp3 = 90, 676,'ABC',78>87, 91/3,
print(tp3, type(tp3))

#lets access the elements of the tuple
print(tp3[3])

#lets print multiple elements
#print 5 seven times
print((5,)*7)

#lets test the immutability of the tuple
'''tp3[3] = 20
print(tp3) '''

#let delete element false from the tuple tp3
'''del tp3[3]
print(tp3)'''

#Tuple concatenation
t1 = 1,2,3
t1 += 4,5
print(t1) 
t2 = 6,7,8,9

t3 = t1 + t2
print(t3)

#unpacking the tuple
a,b,c,d = t2
print(a,b,c,d)