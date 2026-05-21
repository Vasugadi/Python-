#print numbers from 1 to 100
for i in range(1,101):
    print(i)

# print numbers from 100 to 1 in steps of 1
for i in range(100,0,-1):
    print(i)

#print the multiplication table of n
n=int(input("Enter a number: "))
for i in range(1,11):
    print(n,"*",i,"=",n*i)

# print the sum of all numbers from 1 to n
n=int(input("Enter a number: "))
sum=0
for i in range(1,n+1):
    sum+=i
print("The sum of all numbers from 1 to",n,"is",sum)    
