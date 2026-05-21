#list a built in data type that stores set of values
#it can store elements of different data types int,float,string etc
#list is mutable
#list is ordered
#list is indexed
#list is iterable
#list is changeable
#list is dynamic
#list is heterogeneous

marks=[87,64,233]
print(marks[0],marks[1],marks[2])

marks[0]=100
print(marks[0])

marks.append(100) #append adds element at the end of the list
print(marks)

marks.insert(0,100)#insert adds element at the specified index
print(marks)

marks.remove(100)#remove removes the specified element
print(marks)

marks.pop(0)#pop removes the element at the specified index
print(marks)

marks.clear()#clear removes all the elements from the list
print(marks)

print(len(marks))#len returns the length of the list
print(type(marks))#type returns the type of the list


slip=[1,2,3,4,5,6,7,8,9,10]
print(slip[0:5])#slicing returns the elements from the specified index to the specified index
print(slip[0:5:2])#slicing returns the elements from the specified index to the specified index with the specified step
print(slip[::-1])#slicing returns the elements from the specified index to the specified index with the specified step
