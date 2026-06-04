# INHERITANCE
# when one class (child/derived) derives the properties & methods of another class (parent/base).

# SINGLE INHERITANCE EXAMPLE
class Car:
    @staticmethod
    def start():
        print("car started..")

    @staticmethod
    def stop():
        print("car stop..")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name=name

car1=ToyotaCar("fortuner")
car2=ToyotaCar("prius")

print(car1.start())




# MULTILEVEL INHERITANCE EXAMPLE
class Car:
    @staticmethod
    def start():
        print("car started..")


    @staticmethod
    def stop():
        print("car stopped..")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand= brand

class fortuner(ToyotaCar):
    def __init__(self,type):
        self.type=type


car1=fortuner("diesel")
car1.start()                            




# MULTIPLE INHERITANCE EXAMPLE
class A:
    varA="welcome to class A"

class B:
    varB="welcome class B"

class C:
    varC="welcome to class C"

class C(A,B):
    varC="welcome to class C"

c1=C()

print(c1.varC)

print(c1.varB)

print(c1.varA)