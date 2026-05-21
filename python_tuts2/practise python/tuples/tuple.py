a=10,20,30 #its a tuple
a=(1,2,3,4)
b=()#its a empty tuple

#len
print(len(a))
#accessing tuple
print(a[0])
print(a[1])
print(a[2])
print(a[3])
#slicing
print(a[1:3])
#concatenation
print(a+b)
#repetition
print(a*3)
#membership
print(2 in a)
#iteration
for i in a:
    print(i)
#tuple unpacking - assigning values to variables
a,b,c,d=a
print(a,b,c,d)
#tuple is immutable
