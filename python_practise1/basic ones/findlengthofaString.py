#using len() function
str="welcome"
print(len(str))

#using for loop
str="welcome"
count=0
for i in str:
    count+=1
print(count)

#using while loop
str="welcome"
count=0
i=0
while i :
    count+=1
    i+=1
print(count)


#
str="welcome"
counter=0
while str[counter:]:
    counter+=1
print(counter)

#
str="welcome"
rand="&"
print(rand.join(str))
print(rand.join(str).count(rand)+1)