class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id


    def showDetails(self):
        print(f"The name of Employee: {self.id} is {self.name}")


class Programmer(Employee):
    def showLanguage(self):
        print("The default Language is Python.")



e = Employee("Roshan Shakya", 2108)
e.showDetails()

f = Employee("Harry", 2845)
f.showDetails()