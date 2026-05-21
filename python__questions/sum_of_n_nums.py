a=int(input("Enter a number: "))

sum=0
while a>0:
    sum=sum+a
    a=a-1
    
print("The sum of n numbers is:",sum)

b=int(input("Enter a number: "))
sum=0
for i in range(1,b+1):
    sum=sum+i

print("The sum of n numbers is:",sum)

c=int(input("Enter a number: "))

def sum_of_n_nums(n):
    if n==0:
        return 0
    else:
        return n+sum_of_n_nums(n-1)

print("The sum of n numbers is:",sum_of_n_nums(c))