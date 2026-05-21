g="1,234"
#isalnum() checks if all characters in the string are alphanumeric
print(g.isalnum())  # False, because of the comma
# isalpha() checks if all characters in the string are alphabetic
print(g.isalpha())  # False, because of the comma and digit
# isdigit() checks if all characters in the string are digits
print(g.isdigit())  # False, because of the comma
# islower() checks if all characters in the string are lowercase
print(g.islower())  # False, because of the uppercase '1'
# isupper() checks if all characters in the string are uppercase
print(g.isupper())  # False, because of the lowercase '234'
#isdecimal() checks if all characters in the string are decimal
print(g.isdecimal())  # False, because of the comma
#is.numeric() checks if all characters in the string are numeric
print(g.isnumeric())  # False, because of the comma
#isspace() checks if all characters in the string are whitespace
print(g.isspace())  # False, because of the digits and comma
# isprintable() checks if all characters in the string are printable
print(g.isprintable())  # True, because all characters are printable
 