#the process is
#1. sort the list
#2. print the second last element of the list

list=[1,2,3,4,5]

list.sort()

print(list[-2])

#
list=[1,2,3,4,5]

my_new=set(list)

my_new.remove(max(my_new))

print(max(my_new))

