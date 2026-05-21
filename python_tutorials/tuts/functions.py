#def func_name(param1,param2):
    #some work
    #return ValueError
#print(func_name(arg1,arg2))

def sum(a,b):
    return a+b
sum(2,3)
sum(5,7)
sum(10,20)

def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
factorial(5) #5*4*3*2*1

def len_of_list(L):
    return len(L)
len_of_list([1,2,3,4,5])    

def print_list(L):
    for i in L:
        print(i,end=" ")
print_list([1,2,3,4,5]) 
print("\n")

# 定义一个函数，用于计算阶乘

def fact(n):
    fac=1
    for i in range(1,n+1):
        fac=fac*i
    print(fac) 
fact(5)

def converter (usd_val):
    inr_val=usd_val*82
    print(usd_val,"usd=",inr_val,"inr")
converter(10)