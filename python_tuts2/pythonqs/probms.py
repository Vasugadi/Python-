a=0
b=1
n=int(input("Enter the number of terms: "))
print("Fibonacci Series:")
if(n ==1):
    print(a)
elif(n == 2):
    print(a,b)
for i in range(2,11):
    c=a+b
    a=b
    b=c
    
    print(c,end=" ")
