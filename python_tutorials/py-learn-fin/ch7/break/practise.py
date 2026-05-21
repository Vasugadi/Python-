#print number from 1 to 10
i=1
while i<=100:
    print(i)
    i+=1
print("done")

#print the multiplication of number n
n=int(input("enter the number:"))
i=1
while i<=12:
    print(n,"*",i,"=",n*i)
    i+=1
print("done")

#print the elements of list using for loop
list=[1,2,3,4,5,6,7,8,9,10]
i=0
while i<len(list):
    print(list[i])
    i+=1
print("done")

#search for number x in list
list=[1,2,3,4,5,6,7,8,9,10]
x=int(input("enter the number:"))
i=0
while i<len(list):
    if x==list[i]:
        print("number found ")
    else:
        print("finding...")
    i+=1
print("done")   

