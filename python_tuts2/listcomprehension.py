#list comphrehension is a concise way to create lists in Python.
l1=["apple","banana","cherry","date"]
l2=[]
for i in l1:
    if(i>45):
        l2.append(i)
    
l3=[i for i in l1 if i>45]  # list comprehension