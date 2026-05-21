a=[1,2,3,4,5]

temp=a[0]
a[0]=a[-1]
a[-1]=temp

print(a)

#
a[0],a[-1]=a[-1],a[0]
print(a)

#using tuple

get=(a[-1],a[0]) #packing

a[0],a[-1]=get

#approach 4 * operand
b=[1,2,3,4,5]
start,*middle,end=b
print(start)
print(middle)
print(end)
# or
b=[end,*middle,start]
print(b)


#approach 5 using pop()
c=[1,2,3,4,5]
first=c.pop(0)
last=c.pop(-1)

c.insert(0,last)
c.append(first)
print(c)