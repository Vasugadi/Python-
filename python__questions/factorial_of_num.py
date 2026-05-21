num=int(input("Enter a number: "))
fac=1

for i in range(1,num+1):
    fac=fac*i
print(fac)

a=int(input("Enter a number: "))
fac=1
if a<0:
    print("Factorial is not defined for negative numbers")
if a==0 or a==1:
    print("Factorial of",a,"is 1")
else:   
    while a>0:
        fac=fac*a
        a=a-1
print(fac)

def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
    
n=int(input("Enter a number: "))

if n<0:
    print("Factorial is not defined for negative numbers")
else:
    print("Factorial of",n,"is",factorial(n))
    
    
    
def factorial(n):
    # tenrary operator
    return 1 if n==0 or n==1 else n*factorial(n-1)