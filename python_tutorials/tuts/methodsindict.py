dict={"name":"vaishu","subj":"softs skills","she":"beauty"}
print(dict.keys())
print(dict.values())
# to typecast the ans in list
print(list(dict.keys()))
print(len(dict))
print(dict.items())
pairs=list(dict.items())
print(pairs[0])
#to know the value of the key
print(dict["name"]) #if its error it gives error
print(dict.get("name")) #if its error it gives none

