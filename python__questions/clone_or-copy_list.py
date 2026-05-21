list=[4,8,2,10,25,28]
#method 1
my_copy=list[:]
print(my_copy)

#method 2
my_copy2=list.copy()
print(my_copy2)
#method 3
my_copy3=[]
list.extend(my_copy3) #extend is used to add elements of one list to another list
print(my_copy3)

#method 4
my_copy4=list(list) #it will create a new list with the same elements as the original list
print(my_copy4)

#method 5
my_copy5=[i for i in list] #it will create a new list with the same elements as the original list
print(my_copy5)