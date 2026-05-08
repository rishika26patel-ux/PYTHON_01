#BREAK & CONTINUE

#@BREAK: used to terminate the loop when encountered

#@CONTINUE: Terminate execution in the current iteration & continue execution of the loop with the next iteration

# BREAK CONDITION
i=1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1

# CONTINUE CONDITION IN LOOP
i=0
while i<=5:
    if(i==3):
        i+=1
        continue #skip
    print(i)
    i+=1  #output is 1,2,4,
    

 #print even numbers in 1 to 10 numbers
i=0
while i<=10:
    if(i%2==0):
        i+=1
        continue #skip
    print(i)
    i+=1


#print even numbers
i=0
while i<=10:
    if(i%2!=0):
        i+=1
        continue #skip
    print(i)
    i+=1    