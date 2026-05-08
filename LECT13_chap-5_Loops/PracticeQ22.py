#Search for a number x in this tuple using loop
#(1,4,9,16,25,36,49,64,81,100)
numb=(1,3,4,6,7,8,9,7,5)

x= 4

i=0
while i < len(numb):
    if(numb[i] == x):
        print("FOUND AT idx",i)
    else:
        print("finding..")
    i += 1
