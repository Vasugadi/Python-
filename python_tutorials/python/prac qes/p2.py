#wap to input users first name and print its length
name=input("entr you name Length is: ")
length=len(name)
print("length of your name is:",length)
print(name[0])
print(name[1])

#write the occurence of dollar in string
name=input("enter the name you want to check: ")
count=name.count("$")
print("the occurence of $ is:",count)

name="babe"
count=0
while(count<len(name)):
    if(name[count]=="b"):
        print("b is present at:",count)
    count+=1
print("the occurence of b is:",count)