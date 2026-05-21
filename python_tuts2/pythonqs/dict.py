#sort a dictionary by value
dict={"gf":"kendall","spouse":"kyli","bitch":"angelina white"}
print(sorted(dict.values()))

#
dict={
}
for i in range(1,11):
    dict[i]=i**2

print(dict)

#multiply all the items in a dict
dict={"a":1,"b":2,"c":3,"d":4,"e":6}
mul=1
for i in dict:  #dict.values()
    mul*=dict[i] #i
print(mul)

for i in dict.values():
    mul*=i
print(mul)

#to sort a dictionary by key
dict={"a":1,"b":2,"c":3,"d":4,"e":5}
print(sorted(dict.keys()))
#to sort a dictionary by value
dict={"a":1,"b":2,"c":3,"d":4,"e":5}
print(sorted(dict.values()))
#to sort a dictionary by key and value
dict={"a":1,"b":2,"c":3,"d":4,"e":5}
print(sorted(dict.items()))