# print the elements of the following list using a loop
a=[1,2,3,4,5,6,7,8,9,10]
for i in a:
    print(i)

# search for a element in the tuple using loop
b=(1,4,9,16,25,36,49,64,81,100)
x= int(input("enter the element to search: "))
idx=0
for i in b:
    if i==x:
        print("element ",i," found at",idx)
        break
    idx+=1
else:
    print("element not found")

