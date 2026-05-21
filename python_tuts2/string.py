a="hello {}world"
b=a.split(" ")
print(b)

print(len(a))
print(a.count("l"))
print(a.upper())
print(a.lower())
print(a.index("l"))
print(a.capitalize())
print(a.casefold()) #case insensitive
print(a.isalpha()) #check if all characters are alphabetic
print(a.isnumeric()) #check if all characters are numeric
print(a.format("world")) #formatting string
print(a.replace("world", "Python")) #replace substring
print(a.center(20)) #center the string in a field of width 20

name="jhon"
b="my name is {}"
print(b.format(name)) #formatting string with variable
print(b.format(name).upper()) #formatting and converting to uppercase
print(name.canter(20,'*'))