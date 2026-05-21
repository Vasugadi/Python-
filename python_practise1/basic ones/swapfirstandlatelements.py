#input=[12,35,9,56,24]
#output=[24,35,9,56,12]

input=[12,35,9,56,24]
output=[]
for i in range(len(input)):
    if i==0:
        output.append(input[-1])
    elif i==len(input)-1:
        output.append(input[0])
    else:
        output.append(input[i])
print(output)

#by using ternary operator

mylist=[12,35,9,56,24]
size=len(mylist)
temp=mylist[0]
mylist[0]=mylist[size-1]
mylist[size-1]=temp
print(mylist)

#by using 
mylist=[12,35,9,56,24]
mylist[0],mylist[-1]=mylist[-1],mylist[0]
print(mylist)

#by using tuple
get=(mylist[-1],mylist[0])
mylist[0],mylist[-1]=get[0],get[1]

#operand
mylist=[12,35,9,56,24]
strt,*middle,end=mylist
mylist=[end,*middle,strt]
print(mylist)

#by using pop method
mylist=[12,35,9,56,24]
first=mylist.pop(0)
print(first)
last=mylist.pop(-1)
print(last)
mylist.append(first)
mylist.insert(0,last)
print(mylist)