# READ IN A FILE


# f =open("demo.txt", "r")
# data= f.read()
# print(data)
# print(type(data))
# f.close()


# f =open("demo.txt", "r")
# data= f.read(5)
# print(data)

# f.close()


# f =open("demo.txt", "r")
# line1= f.readline()
# print(line1)


# line2= f.readline()
# print(line2)

# f.close()




# WRITING TO A FILE

# f= open("demo.txt","w")
# f.write("this is a new line")  #overwrites the entire file


# f= open("demo.txt","a")
# f.write("\nthis is a new line")  #adds to the file


# create a new file automatically using append and w
# f= open("sample.txt","a")
# f.close()

# f= open("demo.txt","r+") #r+ used to overwrite in existing data(no truncate)
# f.write("abc")
# print(f.read())
# f.close()


# f= open("demo.txt","w+") #w+ read and  wrie and truncate the data
# f.write("abc")
# print(f.read())
# f.close()


# f= open("demo.txt","a+") #a+ read and  append ponter end me hoga(no truncate)
# f.write("abc")
# print(f.read())
# f.close()



# WITH SYNTAX
# with open("demo.txt","r") as f:  #isme automatic close hoti hai file likhna niii padta
#     data=f.read()
#     print(data)


# with open("demo.txt","w") as f:  #isme automatic close hoti hai file likhna niii padta
#    f.write("new data")
# print(data)    





# DELETING A FILE
# using the os module

# module(like a code library) is a file written by another programmer that generally has a function we can use.

# import os

# os.remove("practice.txt")





# PRACTICE QUESTIONS..............

# Q1
# CRAETE A NEW FILE "PRACTICE.TXT" USING PYTHON.ADD THE FOLLOWING DATA IN IT.

# Hi everyone
# we are learning file i/o
# using java.
# i like programming in java


# with open("practice.txt","w") as f:
#     f.write("Hi everyone\n we are learning File I/O\n")
#     f.write("using java\n i like programming in java")




# Q2
# WAF that replace all occurance of java with python in above file

# with open("practice.txt","r") as f:
#     data= f.read()

# new_data=data.replace("java","python")
# print(new_data)    

# with open("demo.txt","w") as f:
#     f.write(new_data)



# Q3
# search if the word "learning" exists in the file or not.

# def check_for_word():
#     with open("practice.txt","r") as f:
#         data= f.read()
#         if(data.find("learning")!=-1):
#             print("FOUND")
#         else:
#             print("NOT FOUND")    

# check_for_word()            





# Q4
# WAF to find in which line of the file does the word "learning" occur first,
# print -1 if word not found.

# def check_for_word():
#     with open("practice.txt","r") as f:
#         data= f.read()
#         if(data.find("learning")!=-1):
#             print("FOUND")
#         else:
#             print("NOT FOUND")    

# check_for_word()            


# def  check_for_line():
#     word="pyr"
#     data=True
#     line_no=1
#     with open("practice.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no+=1

#     return -1

# print(check_for_line())            





# Q5
# From a file containing numbers seprated by comma,print the count of even numbers
count=0
with open("demo.txt","r") as f:
    data=f.read()
    

    nums=data.split(",")
    for val in nums:
        if(int(val) % 2==0):
            count+=1

print(count)