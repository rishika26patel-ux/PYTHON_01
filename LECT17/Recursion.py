#recursion 
#when a function calls itself repeatedly
#SYNTAX


#for example- print n to 1 backword
def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)

show(5)    