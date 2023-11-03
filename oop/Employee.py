class Employee:
    """This is the class for the employee"""
    #class variable
    empCount = 0

    #lets add an initializer or constructor
    def __init__(self, name,salary):
        """Initialize the employee"""
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    #lets define member functions
    def displayCount(self):
        """Returns total number of employees"""
        print("Total number of employees are %d " %Employee.empCount)

    #Displays the employee details
    def displayEmployee(self):
        print("Name: ",self.name+"\nSalary: ",self.salary)

#lets create objects for each employee
pavan = Employee("pavan",45000)
print(pavan.displayCount())
print(pavan.displayEmployee())
