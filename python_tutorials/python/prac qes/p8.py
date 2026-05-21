list=[1,4,9,16,25,36,49,64,81,100]

for i in list:
    print(i)

idx=0
x=int(input("enter the value of x: "))
for el in list:
    if el==x:
        print("element found",idx)
        break
    idx+=1
      
    print(el)
else:
    print("element not found")