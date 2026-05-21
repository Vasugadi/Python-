#methods sets
collection=set()
print(type(collection))

collection.add("city:vizag")
collection.add("state:amaravati")
collection.add("country:india")
collection.add("continent:asia")
collection.add("country:india")

print(collection)

collection.remove("country:india")
print(collection)

collection.discard("country:india")
print(collection)

collection.clear()
print(collection)

collection2={"city:vizag","state:amaravati","country:india","continent:asia"}
print(collection2)
print(collection2.pop())

#union
set1={1,2,4,5}
set2={2,3,4,6}
print(set1.union(set2))
#intersection
print(set1.intersection(set2))

data={
}

data.update({"name":"sai","age":23})
print(data)