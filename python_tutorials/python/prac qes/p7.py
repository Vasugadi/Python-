list=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(list):
    print(list[i])
    i=i+1

print("koy koy kodni")




# wap to print 1 to 100
i=1
while i<=100:
    print(i)
    i=i+1
print("*********")

#print numbers form 100 to 1
i=100
while i>=0:
    print(i)
    i=i-1

print("*********")

n=int(input("enter the number:"))
i=1
while i<=12:
    print(n,"*",i,"=",n*i)
    i=i+1
print("*********")

# print the elements of the following list using  a loop


tup=(1,2,3,4,5,6,7,8,9,10)
i=0
x=int(input("enter the number: "))
while i<len(tup):
    if(tup[i]==x):
        print("found at",i)
    else:
        print("finding...")
        
    i=i+1


#using break and continue
i=0
while i<10:
    if(i==5):
        break
    i=i+1

# continue
i=0
while i<10:
    if(i==5):
        continue
    i=i+1

i=1
while i<=10:
    if(i%2==0):
        continue
    print(i)
    i=i+1