list=[1,2,3,4,5,6]
print(f'Before list {list}')
list[0]=10
print(f'After list {list}')
#slicing
lst=[1,2,3,4,5]
lst[0:3]=10,20,30
print(lst)

#concatenation
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
result=list1+list2
print(result)
list3=[list1,list2]
print(list3)
      
#
lst=[1,2,3,4,5]
print(lst*5)

#membership
lst=[1,2,3,4,5]
print(1 in lst)
print(6 in lst)
print(1 not in lst)
print(6 not in lst)

list_1=[1,2,3,4,5]
check=int(input("enter a number to check= "))
if check in list_1:
    print("yes")
else:
    print("no")
    
#alias
list_1=[1,2,3,4,5]
list_2=list_1
list_2[0]=10
print(list_1)
print(list_2)

#copymethod
list_1=[1,2,3,4,5]
list_2=list_1.copy()
list_2[0]=10
print(list_1)

#append
a=[1,2,3]
b=[4,5,6]
a.append(b)
print(a)

#extend - add all elements of list to another list
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)

#insert
a=[1,2,3]
a.insert(1,10)
print(a)

#remove
a=[1,2,3,4,5]
a.remove(3)
print(a)

#pop
a=[1,2,3,4,5]
a.pop(1)
print(a)

#del
a=[1,2,3,4,5]
del a[1]
print(a)

#CLEAR 
a=[1,2,3,4,5]
a.clear()
print(a)

#count
a=[1,2,3,4,5,1,1,1,1]
print(a.count(1))

#index
a=[1,2,3,4,5,1,1,1,1]
print(a.index(1))

#reverse
a=[1,2,3,4,5]
a.reverse()
print(a)

#to create a null list
a=[]
print(a)

#to create a list with single element
a=[1]
print(a)


#
a=[1,2,3,4,5]
counter=a.count(1)
print(counter)

#sort
a=[7,1,2,3,4,5]
a.sort()
#sort(reverse=True)
print(a)

#min
print(min(a))

#max
print(max(a))

#sum
print(sum(a))

#len
print(len(a))

#list comprehension
a=[1,2,3,4,5]
b=[i*i for i in a]
print(b)
#b=[i*i for i in a if i%2==0]
#print(b)

#union
a=[1,2,3,4,5]
b=[6,7,8,9,10]
print(set(a).union(set(b)))

#intersection
print(set(a).intersection(set(b)))

#set function - is used to remove duplicate elements

#nested list
a=[1,2,3,[4,5,6]]
print(a[3][1])


#range 
a=list(range(1,10))
print(a)

#[expression for item in iterable if condition]
source=[]
for i in range(1,10):
    source.append(i**2)
print(source)

source=[i**2 for i in range(1,10) if i%2==0]
print(source)


