#0  1 1 2 3 5 8 13 21 34
#n1 n2

n1=0
n2=1

print(n1)
print(n2)
for i in range(2,10):
    n3=n1+n2
    print(n3)
    n1=n2
    n2=n3
    

#fibonacci series using recursion
def fibo(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)# 10= fibo(9)+fibo(8)
print(fibo(10)) 
    
    
    