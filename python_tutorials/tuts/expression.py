#string and numeric can operate with *
a,b=2,3
txt="@"
print(a*txt*b)

#string and string can operate with +
a,b="hello","world"
print(a+b)

#string and numeric cannot operate with +
#a,b="hello",2
#print(a+b)

#numeric values can operate with all arithmetic operators
a,b=2,3
c=4
print(a+b*c) #14

#arithmetic expression 
a,b=10,5.0
c=a*b
print(c)