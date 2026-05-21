# d=open(".txt","r")
# data=d.read()
# print(data)
# num=""
# for i in range(len(data)):
#     if(data[i]==","):
#         print(int(num))
#         num=""
#     else:
#         num+=data[i]
count=0
with open("p3.txt","r") as f:
    data=f.read()
    print(data)
    nums=data.split(",")
    print((nums))
    for i in nums:
        if(int(i)%2==0):
            count+=1
print(count)