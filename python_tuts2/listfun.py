list=["Apple","banana","cherry","date"]
for i in list:
    print(i)

(print(i) for i in list)

for i in range(len(list)):
    print(list[i] )

i=0
while i<len(list):
    print(list[i])
    i+=1

# function used in list
# to print the lenth of the list
print(len(list))
# to print the frequency of an element in the list
print(list.count("banana"))
# to add an element to the list
list.append("strawberry")
# to insert an element at a specific position
list.insert(1,"orange")
# to remove an element from the list
list.remove("date")
# to pop an element from the list
list.pop(2) #it will remove the element at a particular index
# to sort the list
list.sort()
# to copy the list
list2=list.copy()
# to reverse the list
list.reverse()
#to extend the list
b=["cap","yup"]
print(b.extend(list))
# to clear the list
list.clear()