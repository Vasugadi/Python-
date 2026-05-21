profile={
    "name":"python",
    "age":100,
    "salary":10000
}
print(profile)

#get : get the value of the key
print(profile.get("name"))
#if key is not present then it will give none
print(profile.get("gender","notfound"))

#keys : get all the keys of the dictionary
print(profile.keys())
print(list(profile.keys()))

#values : get all the values of the dictionary
print(profile.values())
print(list(profile.values()))

#items : get all the items of the dictionary
print(list(profile.items()))

#pop 
print(profile.pop("age","not found"))

#clear
profile.clear()
print(profile)

#dict comprehension
squares = {x: x*x for x in range(6)}
print(squares)

#add 
profile.update({"age":100})
print(profile)

#
for k in profile.values():
    print(k)
    
for k in profile.keys():
    print(k)

for k in profile.items():
    print(k)
    