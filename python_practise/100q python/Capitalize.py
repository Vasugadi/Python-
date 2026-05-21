#to capitalize given word
str="hello world" 
for i in str:
    print(i.capitalize(),end="")


#to capitalize given sentence
str="hello world"
#it will capitalize the first letter of the sentence
print(str.capitalize())
#to capitalize all the given string
str="hello world"
print(str.upper())

#to capitalize the sentence
str="hello world"
print(str.title())

#to capitalize the first letter of each word
str="hello world are u okay"
print(str.title())

#to swap the case of the given string
str="Hello World Are U Okay"
print(str.swapcase())

#to capitalize all the vowels in capital
def capitalize_vowels(string):
    vowels="aeiou"
    for i in string:
        if i in vowels:
            print(i.upper(),end="")
        else:
            print(i,end="")
string="hello world"
capitalize_vowels(string)

