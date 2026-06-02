# private(like) attributes and methods
# conceptual attributes and methods are meant to be used only within the class and are not accessible from outside the class

class Person:
    __name="risuu"

    def __hello(self):#__is used to private class or methods
        print("hello person")

    def welcome(self):
        self.__hello()

p1=Person()

print(p1.welcome())
