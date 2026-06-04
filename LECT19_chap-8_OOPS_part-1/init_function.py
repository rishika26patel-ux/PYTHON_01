# --init-- function

# CONSTRUCTOR
# All classes have a function called _init_(),which is always executed when the object is being initiated

# CREATING CLASS                        CREATING OBJECT
# class Student:                         s1=Student("rishika")
#    def __init__(self,fullname):        print(s1.name)
    #   self.name=fullname

#  (*The (self) parameter is a reference to the curent instance of the class,and is used to access variables that belongs to the class)

# python language automatic init function create karti hai or usko execute karti hai

# CREATE A CONSTRUNCTOR 

class Student:
    name="rishika"
    def __init__(self,fullname):  #constructor ke andar humesha argument pass karna hota hai ,self is a  first parameter
        self.name=fullname
        print("adding new student in database")

s1=Student("rishika")
print(s1.name)  #parnathesis constructor call karne ke liye


s2=Student("rika")
print(s2.name) #constructor har ek object ke sath call hota hai







class Student:
    name="rishika"
    def __init__(self,fullname,marks):  #constructor ke andar humesha argument pass karna hota hai ,self is a  first parameter
        self.name=fullname
        self.marks=marks
        print("adding new student in database")

s1=Student("rishika",99)
print(s1.name,s1.marks)  #parnathesis constructor call karne ke liye


s2=Student("rika",90)
print(s2.name,s2.marks) #constructor har ek object ke sath call hota hai







class Student:


    # default constructor
    def __init__(self):
       pass
    
    #parameterized constructor (self ke alawa bhi or parameter hote hai)

    def __init__(self,fullname,marks):  #constructor ke andar humesha argument pass karna hota hai ,self is a  first parameter
        self.name=fullname
        self.marks=marks
        print("adding new student in database")

s1=Student("rishika",99)
print(s1.name,s1.marks)  #parnathesis constructor call karne ke liye


s2=Student("rika",90)
print(s2.name,s2.marks)