num=int(input("eneter the number: "))
div=int(input("enter the divisor: "))
list=[]
for i in range(num):
    if i%div==0:
        list.append(i)

print(list)
    
#lambda function temp
#filter 
li=[39,48,26,98,33,67,87]
result=list(filter(lambda x : x % 13 == 0,li))
print(result)