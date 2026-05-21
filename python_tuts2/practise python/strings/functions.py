str="python is a programming language"
# str=input("enter your name: ").titl()
# its converts to uppercase
print(str.upper())
# its converts to lowercase
print(str.lower())
# its converts to titlecase
print(str.title())
# its converts to capitalize
print(str.capitalize())
#swap case -its converts to uppercase to lowercase and vice versa
print(str.swapcase())
#find -it returns the index of the first occurence of the specified value
print(str.find("a"))
#replace -it replaces a specified phrase with another specified phrase
print(str.replace("python","java"))
#count -it returns the number of times a specified value occurs
print(str.count("a"))
#split- it splits a string into a list where each word is a list item
a=str.split()
print(a)
#startswith -it checks if a string starts with the specified value
print(str.startswith("p"))
#endswith -it checks if a string ends with the specified value
print(str.endswith("e"))
#join -it joins the elements of an iterable to the string
print(" .. ".join(a))
#isalpha - if the value is not alpha
print(str.isalpha())
#isalnum - if the value is not alphanumeric
print(str.isalnum())
#isdecimal - if the value is not decimal
print(str.isdecimal())
#isdigit - if the value is not digit
print(str.isdigit())
#isidentifier - if the value is not identifier
print(str.isidentifier())
#islower - if the value is not lower
print(str.islower())
