dict={"name":"shradha", 
      "score":{"maths":90,"english":80,"science":70}}
print(dict)
print(list(dict.keys()))
print(list(dict.values()))
print(list(dict.items()))#tuple
print(dict["score"]["maths"])
print(dict["score"][ "english"])
print(len(dict.keys()))
print(dict.get("name"))

pairs=list(dict.items())
print(pairs)
print(pairs[0])
print(pairs[0][0])
print(pairs[0][1])
print(pairs[1][0])
print(pairs[1][1])

dict.update({"name":"marco"})
print(dict)

#print(dict["name1"]) it will print error
print(dict.get("name1"))# gives None

