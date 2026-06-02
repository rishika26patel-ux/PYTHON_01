# STATIC METHODS
# methods that dont use the self parameter(work at class level)

# Class Student:  (decorator)
# @staticmethod
# def college():
# print("global college")


# ..decorators allows us to wrap another function in order to extend the behaviour of thr wrapped function,without permanently modifying it


# then create a method to print the average



class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    @staticmethod
    def hello():
        print("hey everone!!")

    def get_avg(self):
        sum=0
        for val in self.marks:
            sum+=val
        print("hy",self.name,"your avg score is:",sum/3)


s1=Student("rishika patel",[99,87,94]) 
s1.get_avg()       
s1.hello()