# CLASS METHOD
# a class method is bound to the class & recieves the class as an implicit first argument.

# **note===>static method cant access or modify class state & generally for utility.

class Person:
    name="rishika"

    def changeName(self,name):
        self.__class__.name="tanu"

p1=Person()
p1.changeName("tanu")
print(p1.name)
print(Person.name)        


# USING CLASS METHODS
class Person:
    name="rishika"
     
    @classmethod  #it is used to change direct attributes  in class
    def changeName(cls,name):
        cls.name=name 
 
p1=Person()
p1.changeName("tanu")
print(p1.name)
print(Person.name)  
