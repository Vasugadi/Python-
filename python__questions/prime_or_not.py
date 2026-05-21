a=int(input("Enter a number: "))

if(a<=1):
    print(a,"is not a prime number")
else:
    for i in range(2,a):
        if(a%i==0):
            print(a,"is not a prime number")
            break
    else:
        print(a,"is a prime number")
        
        
b=int(input("Enter a number: "))
count=0
if(b<=1):
    print(b,"is not a prime number")
else:
    for i in range(2,b):
        if(b%i==0):
            count+=1
            break
    if(count==0):
        print(b,"is a prime number")
    else:
        print(b,"is not a prime number")