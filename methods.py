# METHODS 
# methods are functinos taht belong to object


# class --> two types -->1data(attributs),2methods(functions)

# CREATING CLASS                   |   CRAETING OBJECT
# class Student:                   |    s1=Student("rishika")
    #def __init__(self,fullname):  |        s1.hello
       #self.name=fullname         | 
                                #  |
     #def hello(self):             |
     # print("hello,self.name")    |



class Student:
    college_name="global college"

    def __init__(self,name,marks):
        self.name=name
        self.marks=marks


    def welcome(self):
       print("welcome student",self.name)


    def get_marks(self):
        return self.marks


s1=Student("rishika",99)
s1.welcome()
print(s1.get_marks())          