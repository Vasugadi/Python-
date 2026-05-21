list=[1,2,3,4,5]
list.sort() #to sort the list in ascending order
print("Smallest element in the list is:",list[0])
print("Largest element in the list is:",list[-1])

list=[1,2,3,4,5]
mi=min(list) #to find the smallest element in the list
mx=max(list) #to find the largest element in the list
print("Smallest element in the list is:",mi)
print("Largest element in the list is:",mx)

smallest=list[0]
largest=list[0]

for i in list:
    if i<smallest:
        smallest=i
    if i>largest:
        largest=i
print("Smallest element in the list is:",smallest)  
print("Largest element in the list is:",largest)