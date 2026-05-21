str1="this is erasood\n i like to play cricket" #\n is used for new line
print(str1)
str2="this is erasood\ti like to play cricket" #\t is used for tab space
print(str2)
str3="this is erasood\b i like to play cricket" #\b is used for backspace
print(str3)
str4="this is erasood\ri like to play cricket" #\r is used for carriage return
print(str4)
str5="this is erasood\\ i like to play cricket" #\\ is used for backslash
print(str5)

# concatenation
str6="this is erasood"
str7="i like to play cricket"
str8=str6+str7
print(str8)

#length
str9="this is erasood"
print(len(str9))

str10=str1+"   "+str2+"    "+str3+"     "+str4
print(str10)

#indexing and slicing
# indexing starts from 0 to n
# space also counts
s="apnacollege"
print(s[0])
print(s[len(s)-1])

#slicing
#slicing is used to get a part of string
#slicing syntax is s[start:end:step]
#step is optional
#step is the number of characters to skip
#step can be positive or negative
#step can be 1 or -1
#step can be any number
#step can be 0
#step can be negative


print(s[0:5])
print(s[-1:-6:-1])
print(s[0:5:2])
print(s[:4]) #is equals to print(s[0:4])
print(s[1:])#is equals to print(s[1:len(s)])
print(s[::2])#is equals to print(s[0:len(s):2]) here 0 is starting len(s) gives ending value and 2 is step value
print(s[::-1])#is equals to print(s[len(s)-1:0:-1]) here -1 is starting len(s)-1 gives ending value and -1 is step value