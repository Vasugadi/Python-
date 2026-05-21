#convert dict to json
import json
data={
    "name":"John",
    "age":30,
    "city":"New York"

}
json_data=json.dumps(data)
print(json_data)

#value of age from json data
d=json.loads(json_data)
print(d["age"])

d=json.dumps[d,indent=4,separator=",",]
print(d)