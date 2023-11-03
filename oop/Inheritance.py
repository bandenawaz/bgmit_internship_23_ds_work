class Parent:
    """Parent Class"""
    parentAttr = 100

    def __init__(self):
        print("Calling parent class constructor")

    def parentMethod(self):
        print("Calling parent class method")

    def setAttr(self, attr):
        Parent.parentAttr = attr

    def getAttr(self):
        print("Parent Attribute: ",Parent.parentAttr)


#Lets create an Child class by inheriting from the parent class
class Child(Parent):
    """Child Class inherited from parent class"""
    #Child class constructor
    def __init__(self):
        print("Calling Child class constructor")

    def childMethod(self):
        print("Calling Child class method")

#Create objects and call all the methods

print(sarthak.parentMethod())
print(sarthak.childMethod())
print(sarthak.getAttr())
print(sarthak.setAttr(200))
print(sarthak.getAttr())
