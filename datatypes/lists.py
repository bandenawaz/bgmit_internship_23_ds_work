'''
List: 
    A list is a data structure that holds an ordered collection of items,
    i.e. we can store a sequence of items in a list.
    The lists are created py placing all items within square brackets([]) 
    and are separated by comma.

    Lists are mutable in nature.
'''

#Lets create a list 
empty_lst = []
print(empty_lst)

#lets create a list with items
prg_lst = ['Python', 'Java', 'JavaScript', 'C++','Kotlin','PHP','Perl']
print(prg_lst)

#Accessing the list of items via index
print(prg_lst[2])

#via negative index
print(prg_lst[-3])

#Accessing multiple items via index
print(prg_lst[1:5])

#Updating list
'''
There are two ways to update the list
1. append(item): This appends the given item to the end of the list
sys: list.append(item)
'''

favFruits = ['Mango','Pineapple','Orange','Banana']
print(favFruits)
#lets add Apple to the list
favFruits.append('Apple')
print("List after adding Apple")
print(favFruits)

#lets add 3 fruits to the list at a time
favFruits.append(['Kiwi', 'DragonFruit','Chickoo'])
print("List after adding multiple fruits")
print(favFruits)

'''
2. extend(list2): This function will add the elements of the list2 to the end of 
the given list 
'''
l2 = ['Kiwi', 'DragonFruit','Chickoo']
favFruits.extend(l2)
print("List after extending")
print(favFruits)

################################################################
#Manipulation of the List
'''
1. insert(index, element):
    It inserts the element at given index into the list
'''

stockList = ['HP','GOOG','TSLA','MSFT','AAPL']
print("The initial list", stockList)

#lets insert Wipro at 3 index
stockList.insert(3,'Wipro')
print("The final list after inserting Wipro at index 3", stockList)

'''
2. remove(element): 
    This function removes the element from the given list
'''
#lets remove the element Wipro from the list
stockList.remove('Wipro')
print("The final list after removing Wipro",stockList)

'''
pop():
    This function removes and returns the last element
    from the list.
'''
stockList.pop()
print(stockList)