n=1
while n<=100:
    print(n)
    n+=1

n=100
while n>=1:
    print(n)
    n-=1

i=1
while i<=12:
    print("2 x",i,"=",2*i)
    i+=1

list=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(list):
    print(list[i])
    i+=1

list=[1,2,3,4,5,6,7,8,9,10]
i=0
x=2
while i<len(list):
    if(list[i]==x):
        print(list[i],"found at index",i)
        break
    else:
        print("finding........")
    i+=1
print("end of the practise session...")

