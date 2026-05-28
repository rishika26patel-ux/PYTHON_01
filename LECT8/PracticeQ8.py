#write a program to find the greatest of 3 numbers entered by the user
a= int(input("enter your first number:"))
b= int(input("enter your second number:"))
c= int(input("enter your third number:"))
d= int(input("enter your forth number:"))

if(a>=b and a>=c):
    print("first number is gratest",a)
elif(b>=c and b>=d):
    print("second number is greatest",b)
else:
    print("third number is greatest:",c)        
