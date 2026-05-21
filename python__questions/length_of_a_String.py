str="hello world"

counter=0
for i in str:
    counter+=1
print(counter)

while str[:]:
    counter+=1
    str=str[1:]
print(counter)

print(len(str))

str="hello world"
random_String="X"

print((random_String).join(str))
print((random_String).join(str).count(random_String)+1)
