#Search for a number x in this tuple using for loop
#(1,2,45,67,89,54,64,25,75)

nums=(1,2,45,67,89,54,64,25,75)

x=2
idx=0
for val in nums:
    if(val==2):
        print("found",idx)
    idx+=1
    
    