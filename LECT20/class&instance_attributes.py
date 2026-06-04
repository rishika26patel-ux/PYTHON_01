# class & instance attributes in python
# (data,name,marks etc)
# class.attr
# obj.attr

# same name ka class attribute or object attributes hota hai to object attribute ki precidence class attributes se higher hoti hai
class Student:
    college_name="global"
    name="rishika"  #class attribute


    def __init__(self,name,marks):
        self.name=name #object attributes
        self.marks=marks
        print("adding new data in database")

s1=Student("tanu,97")
print(s1.name) #tanu output       