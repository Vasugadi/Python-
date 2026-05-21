num=int(input("enter the number: "))
if num>1:   
    for i in range(2,num):
        if(num%i==0):
            print("not prime")
            break
    else:
        print("prime")
else:
    print("not prime")

    
#by using while
i=2
while(i<num):
    if(num%i==0):
        print("not prime")
        break
    i+=1
else:
    print("prime")
    
#
num=5
count=0
if num>1:
    for i in range(2,num+1):
        if(num%i==0):
            count+=1
    if count==1:
        print("prime")
    else:
        print("not prime")
else:
    print("not prime")
    
#by using function
def checkPrime(num):
    count=0
    if num>1:
        for i in range(1,num+1):
            if(num%i==0):
                count+=1
        if count==2:
            print("prime")
        else:
            print("not prime")
    else:
        print("not prime")
        
num=int(input("enter the number: "))
checkPrime(num)