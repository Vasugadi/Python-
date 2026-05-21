mylist=[1,6,3,5,3,4]
x=5
for i in range(0,len(mylist)):
    if mylist[i]==x:
        print("the element found at index:",i)
        break
else:
    print("element not found")
    
def findElement(mylist,x):
    for i in range(0,len(mylist)):
        if mylist[i]==x:
            return i
    return -1
mylist=[1,6,3,5,3,4]
x=5
print(findElement(mylist,x))

#using in operator
mylist=[1,6,3,5,3,4]
x=5
if x in mylist:
    print("element found")
else:
    print("element not found")
    
#ternary 
mylist=[1,6,3,5,3,4]
x=5
print("element found") if x in mylist else print("element not found")

#using flag
mylist=[1,6,3,5,3,4]
x=5
flag=False
for i in range(0,len(mylist)):
    if mylist[i]==x:
        print("element found")
        flag=True
        break
if flag==False:
    print("element not found")


#