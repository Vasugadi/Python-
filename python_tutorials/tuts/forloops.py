li=[1,2,3,4,5,6]
for i in li:
    print(li)
else:
    print("done")

str="apnacollege"
for i in str:
    if(i=="a"):
        print("a found")
        break
    print(i)

print("end")

lis=[1,4,9,16,25,36,49,64,81,100]
for i in lis:
    print(i)

tup=(1,4,9,16,25,36,49,64,81,100)
idx=0
for i in tup:
    if(i==9):
        print("i found at",i,"at index",idx)
        break
    else:
        print("not found")
    idx=idx+1