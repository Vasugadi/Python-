#set is the collection of the unordered items
# each element in  the set must be unique & immutable

nums={1,2,3,4}
set2={"a","b"}

#
null_Set=set()

#set is mutable
nums.add(5)
print(nums)

collection={1,2,3,4,5,"hello","world"}
print(collection)
print(type(collection))
print(len(collection))

#set is unordered
print(collection[0]) #error

#set is immutable
#collection[0]=10 #error

#set is unique
collection.add(1) #no error
print(collection)

#set is mutable
collection.remove(1)
print(collection)

#set is mutable
collection.discard(1)
print(collection)

#set is mutable
collection.pop()


collection.clear()
print(collection)

#set is mutable
collection.update([1,2,3,4,5,6,7,8,9,10])

print(len(collection))

print(collection.pop()) #print any random value in the collection ser

#set methods
#1. set.union
#2.set.intersection

set1={1,2,3,4,5,6,7,8,9,10}
set2={1,11,12,13,14,15}
print(set1.union(set2))