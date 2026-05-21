str=input("enter the string : ")
print(str)
result=""
for char in str:
    if 'a' <= char <= 'z': 
        # If it's a lowercase letter, convert it to uppercase
        result += chr(ord(char) - 32)
    else:
        # If not a lowercase letter, keep the character as is
        result += char

# Output the result
print(result)


###ord() function returns an integer representing the Unicode character.
###chr() function returns a string representing a character whose Unicode code point is the integer.
#chr is used to convert an integer to a character and ord is used to convert a character to an integer.
#ord('a') returns 97 and chr(97) returns 'a'
