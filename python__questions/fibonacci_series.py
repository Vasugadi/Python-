a=int(input("Enter a number: "))

num1=0
num2=1

for i in range(1,a+1):
    print(num1,end=" ")
 #1 2 3  5
     #1 #1 2
    num3=num1+num2
    num1=num2
    num2=num3
    # num1,num2=num2,num2+num1 #1 #2  3
    
print("\n")
n1=0
n2=1
print(n1)
print(n2)
for i in range(2,a):
    sum=n1+n2
    print(sum)
    n1=n2
    n2=sum
