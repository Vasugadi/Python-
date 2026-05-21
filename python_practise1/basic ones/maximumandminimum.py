#input=arr[1,2,3,4,5,6,7,8,9,10]
#Outpu=20
#output=4

arr=[1,2,3,4,5,6,7,8,9,10]
max=arr[0]
min=arr[0]
for i in range(len(arr)):
    if arr[i]>max:
        max=arr[i]
        
    if arr[i]<min:
        min=arr[i]
        
print(min)
print(max)  

