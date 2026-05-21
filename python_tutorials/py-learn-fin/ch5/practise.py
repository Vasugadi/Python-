# store the following in a python dictionary

table ={
    "a piece of furniture":"list of facts and figures",
    "Cat":"a small animal"

}

print(table)

#wap to enter marks of 3 subjects from the user and store them in a
#dictionary and display them and empty the dictionary and add one by one
# use subject name as key and marks as value

x=int("entr the value for first")
y=int("enter 2nd one")
z=int("enter 3rd one")

marks={
    "maths":x,
    "english":y,
    "science":z

}

print(marks)

marks.clear()

marks["maths"]=x
marks["english"]=y
marks["science"]=z

print(marks)
marks.clear()


marks.update({"maths":x,"english":y,"science":z})

print(marks)