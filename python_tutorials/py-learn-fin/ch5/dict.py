dictionary={
    "name":"Rahul",
    "age":23,
    "city":"Mumbai",
    "country":"India",
    "degrees":["BA","bl","MA"],
    "topics":["Python","Java","C++","C#"]
}
print(dictionary)
#dictionaries are unordered and mutable and they dont allow duplicate keys

print(dictionary["name"])
print(dictionary["degrees"])

dictionary["name"]="Rahul Kumar"
dictionary["moto"]="Be Positive"
print(dictionary)

#null dict
null_dict={}
print(null_dict)

#nested dictionary
student={
    "name":"Rahul",
    "age":23,
    "city":"Mumbai",
    "country":"India",
    "subjects":{
        "maths":90,
        "english":85,
        "science":95
    }
}
print(student["subjects"]["maths"])
