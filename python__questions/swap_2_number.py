a=5
b=3
a,b=b,a
print("a=",a)
print("b=",b)

#another method
temp=0
temp=a
a=b
b=temp
print("a=",a)
print("b=",b)

#another method
a=5
b=3
a=a+b
b=a-b
a=a-b

#another method
a=5 #binary 0101
b=3 #binary 0011
#    -0110

#xor operator --  > if both bits are same then it results 0 and if both bits are different then it results 1
a=a^b #XOR operator it results  the value to a is 6 and b is 6
b=a^b #XOR operator it results  the value to b is 5 and a is 6 
a=a^b #XOR operator it results  the value to a is 3 and b is 5

print("a=",a)
print("b=",b)