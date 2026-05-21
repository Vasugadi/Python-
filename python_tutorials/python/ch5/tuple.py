# a built in datatype that lets us create immutable sequence of values
# tuple is immutable
tup=(23,23,34,5,46,89)
print(tup)
#tup[0]=5 is not allowed in python
print(type(tup))

# to find the occurence
print(tup.index(5))

#to find the number of occurences
print(tup.count(5))

# to find the length of the tuple
print(len(tup))

# to find the max value
print(max(tup))

# to find the min value
print(min(tup))

# to find the sum of all the values
print(sum(tup))

# to find the average of all the values
print(sum(tup)/len(tup))
