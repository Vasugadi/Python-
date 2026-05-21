arr=[1,2,3,4,5]
tar=int(input("Enter the number to search in array: "))

for i in arr:
    if(i==tar):
        print("The number is found in array at index:",arr.index(i))
        break
else:    print("The number is not found in array")


flag=0
for i in arr:
    if i == tar:
        print("Found")
        flag=1
        break
if flag==0:
    print("Not Found")
    
    
#using in operator

if tar in arr:
    print("Found")
else:
    print("Not Found")