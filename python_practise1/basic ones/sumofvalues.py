#input arr[]={1,2,3,4,5,6,7,8,9,10}

arr= [1,2,3,4,5,6,7,8,9,10]
sum = 0
for i in range(len(arr)):
    sum = sum + arr[i]
print(sum)
#shortcut is sum(arr)= 55
#max(arr)= 10
#sum(arr,10)= 65
#sum(arr,-10)=45
def sumOfValues(arr):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    return sum
arr= [1,2,3,4,5,6,7,8,9,10]
print(sumOfValues(arr))