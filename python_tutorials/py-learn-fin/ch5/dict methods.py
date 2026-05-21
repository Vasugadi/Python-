#metthods'

dict={
    "name":"sahil",
    "age":20,
    "city":"delhi",
    "hobby":"cricket"

}
print(dict.keys())
print(dict.values())
#too type casste
print(list(dict.keys()))

#to print length
print(len(dict))
print(list(dict.keys()))

#to print all the key,value of the dictionary
print(dict.items())

# to print all the key,value of the dictionary in list form
print(list(dict.items()))

#returns the key according to the value
print(dict.get("age")) 

#to print the value according to the key
print(dict["name"])

#inserts specified items to the dictionary
dict.update({"name":"sahol"})
print(dict)

pairs=list(dict.items())
print(pairs)
print(pairs[0])

print(dict.get("name"))
print(dict["name"])

print(dict.get("kame"))#none
print(dict["lame"])#error


