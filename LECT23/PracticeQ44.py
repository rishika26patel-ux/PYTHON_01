# QS==> define a employee class with attributes role,department and salary.
# this class also has a showDetails() method.
# craete an engineer class that inhert properties from employee and has additional attributes :name and age

class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary

    def showDetails(self):
        print("role=",self.role)
        print("dept=",self.dept)
        print("salary=",self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name= name
        self.age=age
        super().__init__("engineer","CSE","80,000")


engg1=Engineer("rishika",20)
engg1.showDetails()
        