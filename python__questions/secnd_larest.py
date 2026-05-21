lst=[70,11,20,4,100]

lst.sort()
print("Second largest element in the list is:",lst[-2])

#method 2
new_list=set(lst)
new_list.remove(max(new_list))
print("Second largest element in the list is:",max(new_list))

#method 3