# slicing technique
# extend 
# list method
# copy() method
# list comrehension

# 1. slicing technique
list=[1,2,3,4,5]
list1=list[:]
print(list1)

# 2. extend it means adding one list to another list
list=[1,2,3,4,5]
list1=[]
list1.extend(list)
print(list1)

# 3. list() method
mylist = [1, 2, 3, 4, 5]
li = list(mylist)  # ✅ This now calls the built-in list() constructor
print(li)          # Output: [1, 2, 3, 4, 5]

# 4. copy() method
list1=[1,2,3,4,5]
list2=list1.copy()
print(list2)

# 5. list comprehension
list1=[1,2,3,4,5]
list2=[i for i in list1]
print(list1)
print(list2)