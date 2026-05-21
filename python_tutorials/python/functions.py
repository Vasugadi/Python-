def  sum(A,b):
    sum=A+b
    return sum
print(sum(1,2))


def avg(list):
    sum=0
    for i in list:
        sum+=i
    return sum/len(list)
print(avg([1,2,3,4,5]))
    

print("apna",end=" ")
print("college",end=" \n")

#def cal_prod(a=2,b):
#    return a*b

#print(cal_prod(2,3)) # it give error because b is not define

def cal_prod(a,b=2):
    return a*b

print(cal_prod(3)) #it give output as 6

#(not defined,defined)

def lengthOflist(list):
    print(len(list))
lengthOflist([1,2,3,4,5])

def listInsingle(list):
    for i in list:
        print(i,end=" ")
listInsingle([1,2,3,4,5])
print()
def factorial(n):
    fac=1
    for i in range(1,n+1):
        fac*=i
    return fac
print(factorial(5))

def usdToInr(money):
    money*=80
    return money
print(usdToInr(10))
    