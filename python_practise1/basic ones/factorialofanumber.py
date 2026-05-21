#5!=1*2*3*4*%=120

factorial=1

num=5

if num<0:
    print("Factorial does not exist for negative numbers")
elif num==0:
    print("Factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("The factorial of",num,"is",factorial)
    # print(f"The factorial of {num} is {factorial}")




num=int(input("enter the number "))
fact=1
if num==0:
    print("the factorial of the number is 1")
elif num<0:
    print("the factorial of the number is not defined")
else:
    for i in range(1,num+1):
        fact=fact*i
print("the factorial of the number is ",fact)

#recursive method
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        #5*5-1*5-2*5-3*5-4=120
        return n*factorial(n-1)
print(factorial(5))

#using math module
import math
print(math.factorial(5))

#using lambda function
fact=lambda n:1 if n==0 else n*fact(n-1)

#using ternary and recursion
def fact(n):
    return 1 if n==0 else n*fact(n-1)
print(fact(5))