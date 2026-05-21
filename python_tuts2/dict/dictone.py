school={"name":"abc","location":"delhi","pincode":110045}
print(school["name"])
sch={"name":("binod","varun"),"location":"delhi"}
sch["name"]=["binod","varun","gaurav"]
print(sch)
print(school["pincode"])

for i in school:
     print(i)

for v in sch:
     print(v)

for i in sch.values():
     print(i)

for i in sch.keys():
     print(i)

for i in sch.items():
     print(i)

for i in sch:
     print(i,sch[i])
#it will value
a=school.get("name")
print(a)

#items
stu=school.items()
print(stu)

#keys
b=school.keys()
print(b)

#values
c=school.values()
print(c)

#copy
b=school.copy()
print(b)

#dictionary functions part2
#setdefault
school.setdefault("name","abc")
print(school)

#update
school.update({"name":"xyz"})
print(school)

#pop
school.pop("name")
print(school)

#popitem
school.popitem()
print(school)

#nested dictionaries
school={"name":"abc","age":20,"address":{"street":"xyz","city":"pqr"}}
print(school)   
print(school["address"]["city"])
print(school["name"])

#update
school.update({"name":"xyz"})
print(school)
