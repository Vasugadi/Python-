collection={1,2,3,4,5}
print(collection)
#to create a empty set
emptyset=set()
print(emptyset)
#to add elements in set
emptyset.add(1)
emptyset.add(2)
emptyset.add(3)
emptyset.add(4)
#to find the length of the dictionary
print(len(emptyset))
#to remove an element from the set
emptyset.remove(3)
print(emptyset)
#to remove an element from the set if it is not present then it will give error
emptyset.discard(3)
print(emptyset)
#to remove an element from the set if it is not present then it will not give error
emptyset.discard(3)
print(emptyset)
#to clear the set values
emptyset.clear()
print(emptyset)
#to delete the set
del emptyset
print(emptyset)
#to find the union of two sets
set1={1,2,3,4,5}
set2={4,5,6,7,8}
print(set1.union(set2))
#to find the intersection of two sets
print(set1.intersection(set2))
#to find the difference of two sets
print(set1.difference(set2))
#to remove a random values
print(set1.pop())
#to check if a value is present in the set
print(1 in set1)
#to check if a value is not present in the set
print(1 not in set1)