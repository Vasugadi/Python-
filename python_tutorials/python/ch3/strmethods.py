#string methods
#1. lower()
#2. upper()
#3. title()
#4. capitalize()
#5. count()
#6. find()
#7. isalpha()
#8. isalnum()
#9. isdigit()
#10. islower()
#11. isupper()
#12. isspace()
#13. istitle()
#14. join()
    
str="Vasu"
print("the lower func",str.lower())
print("the upper func",str.upper())
print("the title func",str.title())
print("the capitalize func",str.capitalize())
print("the count func",str.count("a"))
print("the find func",str.find("a"))
print("the isalpha func",str.isalpha())
print("the isalnum func",str.isalnum())
print("the isdigit func",str.isdigit())
print("the islower func",str.islower())
print("the isupper func",str.isupper())
print("the isspace func",str.isspace())
print("the istitle func",str.istitle())
str.join("a") # the join function is unavailable for strings

print("the join func",str)

#some more functions
print(str.endswith("u"))
print(str.startswith("v"))
print(str.count("a"))#counts the occurence
print(str.replace("a","b"))#replaces the character
print(str.split("a"))#splits the string
