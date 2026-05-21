print(10/3)
print(10//3)
print(10.5//3)

str= "Hello, World!"

print(str[0:5])
print(str[2:5])
print(str[2:])
print(str[:5])
print(str[:])
print(str[-5:-2])

print(str.upper()) #Converts the string to uppercase
print(str.lower()) #Converts the string to lowercase
print(str.isupper()) #Checks if the string contains uppercase characters
print(str.islower()) #Checks if the string contains lowercase characters
print(str.isalpha()) #Checks if the string contains only alphabetic characters
print(str.isalnum()) #Checks if the string contains only alphanumeric characters
print(str.isdigit()) #Checks if the string contains only digits
print(str.isspace()) #Checks if the string contains only whitespace characters
print(str.startswith('Hello')) #Checks if the string starts with the specified value
print(str.find('World')) #Finds the first occurrence of the specified value
print(str.count('world')) #Counts the number of occurrences of the specified value
print(str[str.find('World'):]) #Extracts a substring from the string
# to reomove the symbols from the string
print(str.replace(',', '')) #Replaces the specified value with another value

