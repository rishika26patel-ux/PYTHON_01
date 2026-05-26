#RECURENCE RELATIONS IN PYTHON
#n= (n-1)!*n


#WRITE A PROGRAM TO RETURN N!

def fact(n):
    if(n==0 or n==1): # base case ya stoping condition
        return 1
    else:
        return n*fact(n-1)

print(fact(4))   