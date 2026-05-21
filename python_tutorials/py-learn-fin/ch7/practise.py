#wap to find sum of n natural numbers
n=int(input("enter the number"))
sum=0
i=0
while i<=n:
    sum=sum+i
    i=i+1
print("the sum of n natural numbers is",sum)


#wap to find factorial of a number
n=int(input("enter the number"))
fact=1
for i in range(1,n+1) :
    fact=fact*i
    i=i+1
print("the factorial of the number is",fact)    