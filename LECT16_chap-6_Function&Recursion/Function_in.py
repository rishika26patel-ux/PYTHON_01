#FUNCTIONS IN PYTHON
#Block of statements that perform a specific task.


#SYNTAX
#def func_name(param1,param2....):
#some work
#return val
# func_name(arg1,areg2...) #function call


#function is reduce redundancy in code
# def calc_sum(a,b):
#     sum=(a+b)
#     print(sum)
#     return sum

# calc_sum(2,10)

# #more lines of code
# calc_sum(3,18)

# #more lines of code
# calc_sum(4,13)

# #more lines of code
# calc_sum(5,1)



#second type to write function
# def sum_of(b,c): #parameters
#     return b+c

# sum=sum_of(4,5) #function call ;(arguments)
# print(sum)




# def print_hello():
#     print("hello")

# print_hello()



# def print_helo():
#     print("helo")

# output= print_helo()
# print(output) #none



# q1  Average of 3 numbers

def avg_of(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg

avg_of(93,95,72)