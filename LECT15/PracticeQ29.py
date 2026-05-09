#WAP to find the factorail of first n numbers.(using for)
n=6
fact=1

for i in range(1,n+1):
   fact*=i

print("factorial=",fact)   


# WAP to find the factorail of first n numbers.(using while)

n=5
fact=1
i=1
while i<=n:
   fact*=i
   i+=1

print("total fac=",fact)