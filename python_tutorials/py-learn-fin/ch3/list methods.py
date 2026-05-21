#various methods in list
list=[1,4,7.9,85,67]
# print(list.count("vasu")) 
# print(list.append("vasu")) #add element at the end
# print(list)
print(list.sort())#sorting in ascending order
print(list)
# print(list.index(7.9)) #find the index of the element
# print(list.remove(7.9)) #remove the element
# print(list.pop(2)) #remove the element at the given index
# print(list)
# print(list.reverse())#reverse the list
print(list.sort(reverse=True))#sorting in descending order
print(list)
# print(list.insert(2,"goluu")) #add element at the given index
# print(list)
print(list.copy())#copy the list
# print(list.clear())#clear the list


#remove and pop methods are used to remove the element from the list
mark=[1,2,3,4,5,6,7,9]
mark.pop(2) 
print(mark)
mark.remove(7)
print(mark)