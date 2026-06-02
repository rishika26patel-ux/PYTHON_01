# PILLERS OF OOPS---->Abstration, Encapsulation,Inheritance,Polymorphism

# ABSTRACTION
# ..Hiding the implementaion detils of a class and only showing the essential features to the user.
class Car:
   def __init__(self):
    self.acc=False
    self.brk=False
    self.clutch=False

   def start(self):
    self.clutch=True
    self.acc=True
    print("car started..")

car1=Car()
car1.start()        


# ENCAPSULATION
# ..Wrapping data nad function into a single unit(object).



