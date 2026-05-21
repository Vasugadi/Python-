count=0
with open("d1.txt","r")as f:
    data=f.read()
    nums=data.split(",")
    for i in nums:
        if(int(i)%2==0):
            count+=1
print(count)