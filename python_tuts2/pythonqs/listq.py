# to swap positions of two elements in a list
list1 = [1, 2, 3, 4, 5]
list1[3], list1[4] = list1[4], list1[3]
for i in list1:
    print(i)

# to add a new element at the index mentioned
ind=int(input("Enter the index where you want to add the element: "))
newel=int(input("entre the new element: "))
list1.insert(ind,newel)
for i in list1:
    print(i)

#to delete an element at the indeex
ind=int(input("enter the index of the element you want to delete: "))
list1.pop(ind)
for i in list1:
    print(i)

#to multiply all the elemnts of the list by a number
num=int(input("Enter the number by which you want to multiply all the elements of the list: "))
list1 = [i * num for i in list1]
for i in list1:
    print(i)

#to print the max element of the list
print("The maximum element in the list is:", max(list1))
list1.sort()
print(list1[-1]) #it returns the largest number

#to print the min element of the list
print("The minimum element in the list is:", min(list1))
#to sort in descending order
list1.sort(reverse=True)
print(list1[-1]) #it returns the smallest number