num=int(input("enter the number: "))
fact=1
if num<0:
    print("enter a positive number")
if num==0:
    print("factorial of 0 is 1")
if num>0:
    for i in range(1,num+1):
        fact=fact*i
print(fact)

#or

#using recursion 
#5!=5*4! which is num-1
num=int(input("enter the number: "))
def fact(num):
    if(num<=1):
        return 1
    if(num==0):
        return 1
    else:
        return num*fact(num-1)

print(fact(num))
