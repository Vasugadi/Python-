set={1,2,3,4,4,5,5,6,6,7,7,8,8,9,9,10}
print(set)
print(type(set))
print(len(set))
print(1 in set)
print(11 not in set)

#functions used in set
#set() function
#to add a value in set
set.add(11)

for c in set:
    print(c)

#add
set.add(11)
print(set)

#update
set.update([11,12,13,14,15])
print(set)
#remove
set.remove(11)
print(set)
#discard
set.discard(11)
print(set)
#pop
set.pop()
print(set)
#clear
set.clear()
print(set) 

#copy
a=set.copy()
print(a)

#part2 functions
a={"ironman","thor","hulk","spiderman"}
b={"ironman","thor","hulk","spiderman","captain america"}
c={"hulk","thor"}
#isdisjoint
print(a.isdisjoint(b))#different values
#issubset
print(a.issubset(b))#is a part
#issuperset
print(a.issuperset(b)) #contains all parts
#intersection
print(a.intersection(b))#have some common values
#union
print(a.union(b))#combines
#difference
print(a.difference(b))#removes values in a which are present in b
#symmetric difference
print(a.symmetric_difference(b))#removes common values and gives the rest 

#update
a.update(b)
print(a)

set.clear()
print(set)
