#FUNCTIONS TYPES IN PYTHON

#//1//               |      //2//
#Built in functions  |       user defined func
#print()             |
#len()               |
#type()              | 
#range()             |


print("rishika") #sep=""
print("patel")#end= "/n"  next line
print("rishika" ,end=" ") #print values in same line


#Calculate multiple of two numbers


#DEFAULT PARAMETER(assume parameters automatically)
def cal_mul(a=2,b=4):
    mul=a*b
    print(mul)
    return mul

cal_mul()