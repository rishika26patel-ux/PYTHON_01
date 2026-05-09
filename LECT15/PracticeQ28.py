#WAP to find the sum of first natural numbers(USING WHILE)
n=int(input("enter number:"))

sum=0
i=1
while i<=n:
      sum+=i
      i+=1

print("total sum=",sum)







#WAP to find the sum of first natural numbers(USING range)

n=int(input("enter number:"))

sum=0
for i in range(1,n+1):
    sum+=i

print("total sum=",sum)
