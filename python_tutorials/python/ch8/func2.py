#function definition
def calsum(a,b):#parameters
    sum=a+b
    print(f"the sum is{a,b} {sum}")
    return sum

calsum(8,9)#function call;arguments

def PrintHello():
    print("hello world")

PrintHello()
PrintHello()
PrintHello()

# in function 2 things are option

# 1 no parameters
# 2 no return
# 3 no return and no parameters

# the function with no return when stored in a variable it will store None

output=PrintHello()
print(output)

# to average
def average(a,b,c):
        sum=a+b+c
        avg=sum/3
        return avg

a=average(5,6,7)
print(a)

def fac(n):
    fac=1
    if n==0 and n==1:
        
        return 1
    else:
        for i in range(1,n+1):
            fac=fac*i
        return fac
n=int(input("enter the value of n:"))
print(fac(n))
print(f"the factorial of {n} is {fac(n)}")
    