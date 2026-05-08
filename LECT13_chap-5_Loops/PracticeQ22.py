#Search for a number x in this tuple using loop
#(1,4,9,16,25,36,49,64,81,100)
tup=(1,4,9,16,25,36,49,64,81,100)
x=25
i=0#initialization
while i<len(tup):
    if(tup[i]==x):
      print("found at idx",i)
else:
   print("finding idx...")
   i+=1
